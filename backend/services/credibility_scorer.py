import google.generativeai as genai
from typing import Dict, List
import json
from collections import Counter
from urllib.parse import urlparse


def extract_domain(url: str) -> str:
    try:
        parsed = urlparse(url)
        domain = parsed.netloc
        if domain.startswith("www."):
            domain = domain[4:]
        return domain
    except:
        return "unknown"


class CredibilityScorer:
    HIGH_CREDIBILITY_DOMAINS = [
        "reuters.com",
        "apnews.com",
        "bbc.com",
        "npr.org",
        "theguardian.com",
        "nytimes.com",
        "washingtonpost.com",
        "wsj.com",
        "economist.com",
        "nature.com",
        "science.org",
    ]

    MEDIUM_CREDIBILITY_DOMAINS = [
        "cnn.com",
        "foxnews.com",
        "msnbc.com",
        "usatoday.com",
        "time.com",
        "newsweek.com",
        "politico.com",
    ]

    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("GEMINI_API_KEY is required")

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    async def analyze(
        self, url: str, title: str, text: str, author: str = "", publish_date: str = ""
    ) -> Dict:
        try:
            domain = extract_domain(url)
            domain_score = self._get_domain_score(domain)

            text_sample = text[:3000]

            prompt = f"""
Analyze the credibility of this news article:

Domain: {domain}
Title: {title}
Author: {author}
Published: {publish_date}

Article excerpt:
{text_sample}

Rate the following on a scale of 0-10:
1. Source Reputation (based on domain)
2. Writing Quality (grammar, professionalism)
3. Evidence Quality (citations, sources mentioned)
4. Objectivity (balanced vs biased language)
5. Transparency (author info, date, clear sourcing)

Also identify:
- Bias direction (left, center, right, or neutral)
- Sensationalism level (low, medium, high)
- Key credibility concerns

Return JSON format:
{{
    "scores": {{
        "source_reputation": 0-10,
        "writing_quality": 0-10,
        "evidence_quality": 0-10,
        "objectivity": 0-10,
        "transparency": 0-10
    }},
    "bias": "left/center/right/neutral",
    "sensationalism": "low/medium/high",
    "concerns": ["concern 1", "concern 2"],
    "strengths": ["strength 1", "strength 2"]
}}
"""

            response = self.model.generate_content(prompt)
            result_text = response.text

            try:
                if "```json" in result_text:
                    result_text = result_text.split("```json")[1].split("```")[0]
                elif "```" in result_text:
                    result_text = result_text.split("```")[1].split("```")[0]

                analysis = json.loads(result_text.strip())
                scores = analysis.get("scores", {})

                score_values = [
                    domain_score,
                    scores.get("source_reputation", 5),
                    scores.get("writing_quality", 5),
                    scores.get("evidence_quality", 5),
                    scores.get("objectivity", 5),
                    scores.get("transparency", 5),
                ]
                overall_score = int((sum(score_values) / len(score_values)) * 10)

                return {
                    "overall_score": overall_score,
                    "domain": domain,
                    "domain_reputation": self._get_domain_reputation(domain),
                    "detailed_scores": scores,
                    "bias": analysis.get("bias", "unknown"),
                    "sensationalism": analysis.get("sensationalism", "unknown"),
                    "concerns": analysis.get("concerns", []),
                    "strengths": analysis.get("strengths", []),
                }

            except json.JSONDecodeError:
                return {
                    "overall_score": domain_score * 10,
                    "domain": domain,
                    "domain_reputation": self._get_domain_reputation(domain),
                    "detailed_scores": {},
                    "bias": "unknown",
                    "sensationalism": "unknown",
                    "concerns": ["Could not complete full analysis"],
                    "strengths": [],
                }

        except Exception as e:
            print(f"Credibility analysis error: {str(e)}")
            return {
                "overall_score": 50,
                "domain": url,
                "domain_reputation": "Unknown",
                "detailed_scores": {},
                "bias": "unknown",
                "sensationalism": "unknown",
                "concerns": [f"Analysis error: {str(e)}"],
                "strengths": [],
            }

    def analyze_bias_distribution(self, articles: List[Dict]) -> Dict:
        sources = [article.get("source", "Unknown") for article in articles]
        source_counts = Counter(sources)

        return {
            "total_articles": len(articles),
            "unique_sources": len(source_counts),
            "source_distribution": dict(source_counts),
            "diversity_score": (
                min(len(source_counts) / len(articles) * 100, 100) if articles else 0
            ),
        }

    def _get_domain_score(self, domain: str) -> int:
        if any(d in domain for d in self.HIGH_CREDIBILITY_DOMAINS):
            return 9
        elif any(d in domain for d in self.MEDIUM_CREDIBILITY_DOMAINS):
            return 7
        else:
            return 5

    def _get_domain_reputation(self, domain: str) -> str:
        score = self._get_domain_score(domain)
        if score >= 8:
            return "High Credibility"
        elif score >= 6:
            return "Medium Credibility"
        else:
            return ""
