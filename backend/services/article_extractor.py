import requests
from newspaper import Article, Config
from bs4 import BeautifulSoup
import re
from typing import Dict
from urllib.parse import urlparse
from datetime import datetime


def extract_domain(url: str) -> str:
    try:
        parsed = urlparse(url)
        domain = parsed.netloc
        if domain.startswith("www."):
            domain = domain[4:]
        return domain
    except:
        return "unknown"


class ArticleExtractor:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }

    def extract(self, url: str) -> Dict:
        try:
            config = Config()
            config.browser_user_agent = self.headers["User-Agent"]
            config.follow_meta_refresh = True
            config.fetch_images = True

            article = Article(url, config=config, language="en")
            article.download()
            article.parse()

            author = "Unknown"
            if article.authors and len(article.authors) > 0:
                author = ", ".join(article.authors)

            publish_date = "Unknown"
            if article.publish_date:
                try:
                    publish_date = article.publish_date.strftime("%B %d, %Y")
                except:
                    publish_date = str(article.publish_date)

            try:
                article.nlp()
                summary = article.summary
                keywords = article.keywords
            except:
                summary = self._generate_simple_summary(article.text)
                keywords = []

            domain = extract_domain(url)
            images_list = list(article.images) if article.images else []

            if author == "Unknown" or publish_date == "Unknown":
                meta_data = self._extract_metadata(url)
                if author == "Unknown" and meta_data.get("author"):
                    author = meta_data["author"]
                if publish_date == "Unknown" and meta_data.get("publish_date"):
                    publish_date = meta_data["publish_date"]

            return {
                "url": url,
                "domain": domain,
                "title": article.title or "No title found",
                "author": author,
                "publish_date": publish_date,
                "text": article.text or "",
                "summary": summary or self._generate_simple_summary(article.text),
                "keywords": keywords,
                "top_image": article.top_image or "",
                "images": images_list[:5],
            }

        except Exception as e:
            print(f"Newspaper3k extraction failed: {str(e)}")
            return self._fallback_extraction(url)

    def _extract_metadata(self, url: str) -> Dict:
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            soup = BeautifulSoup(response.content, "html.parser")

            metadata = {"author": None, "publish_date": None}

            author_selectors = [
                {"name": "author"},
                {"property": "article:author"},
                {"property": "og:article:author"},
                {"name": "byl"},
                {"name": "parsely-author"},
            ]

            for selector in author_selectors:
                author_tag = soup.find("meta", attrs=selector)
                if author_tag and author_tag.get("content"):
                    metadata["author"] = author_tag.get("content")
                    break

            if not metadata["author"]:
                author_patterns = [
                    soup.find("span", class_=re.compile(r"author", re.I)),
                    soup.find("a", class_=re.compile(r"author", re.I)),
                    soup.find("div", class_=re.compile(r"author", re.I)),
                    soup.find("p", class_=re.compile(r"byline", re.I)),
                ]
                for pattern in author_patterns:
                    if pattern:
                        metadata["author"] = pattern.get_text().strip()
                        for prefix in ["By ", "by ", "BY "]:
                            if metadata["author"].startswith(prefix):
                                metadata["author"] = metadata["author"][len(prefix) :]
                        break

            date_selectors = [
                {"property": "article:published_time"},
                {"name": "publication_date"},
                {"name": "publishdate"},
                {"property": "og:published_time"},
                {"name": "date"},
                {"itemprop": "datePublished"},
            ]

            for selector in date_selectors:
                date_tag = soup.find("meta", attrs=selector)
                if date_tag and date_tag.get("content"):
                    try:
                        date_str = date_tag.get("content")
                        date_obj = self._parse_date(date_str)
                        if date_obj:
                            metadata["publish_date"] = date_obj.strftime("%B %d, %Y")
                            break
                    except:
                        continue

            if not metadata["publish_date"]:
                time_tag = soup.find("time", datetime=True)
                if time_tag:
                    try:
                        date_str = time_tag.get("datetime")
                        date_obj = self._parse_date(date_str)
                        if date_obj:
                            metadata["publish_date"] = date_obj.strftime("%B %d, %Y")
                    except:
                        pass

            return metadata

        except Exception as e:
            print(f"Metadata extraction error: {str(e)}")
            return {"author": None, "publish_date": None}

    def _parse_date(self, date_str: str) -> datetime:
        date_formats = [
            "%Y-%m-%dT%H:%M:%S%z",
            "%Y-%m-%dT%H:%M:%S.%f%z",
            "%Y-%m-%d %H:%M:%S",
            "%Y-%m-%d",
            "%B %d, %Y",
            "%b %d, %Y",
            "%d %B %Y",
            "%d %b %Y",
        ]

        date_str = re.sub(r"\+\d{4}$", "", date_str)
        date_str = re.sub(r"Z$", "", date_str)

        for fmt in date_formats:
            try:
                return datetime.strptime(date_str.strip(), fmt)
            except:
                continue

        return None

    def _fallback_extraction(self, url: str) -> Dict:
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            soup = BeautifulSoup(response.content, "html.parser")

            title = soup.find("title")
            title = title.get_text().strip() if title else "No title found"

            metadata = self._extract_metadata(url)
            author = metadata.get("author") or "Unknown"
            publish_date = metadata.get("publish_date") or "Unknown"

            meta_desc = soup.find("meta", attrs={"name": "description"})
            summary = meta_desc["content"] if meta_desc else ""

            paragraphs = soup.find_all("p")
            text = " ".join([p.get_text().strip() for p in paragraphs])

            domain = extract_domain(url)

            return {
                "url": url,
                "domain": domain,
                "title": title,
                "author": author,
                "publish_date": publish_date,
                "text": text[:5000] if text else "",
                "summary": summary or self._generate_simple_summary(text),
                "keywords": [],
                "top_image": "",
                "images": [],
            }
        except Exception as e:
            print(f"Fallback extraction failed: {str(e)}")
            raise Exception(f"Could not extract article content: {str(e)}")

    def _generate_simple_summary(self, text: str, sentences: int = 3) -> str:
        if not text:
            return ""

        sentences_list = re.split(r"[.!?]+", text)
        sentences_list = [s.strip() for s in sentences_list if len(s.strip()) > 20]

        return ". ".join(sentences_list[:sentences]) + "." if sentences_list else ""
