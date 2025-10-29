import requests
from typing import Dict, List, Optional


class NewsSearcher:
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("NEWSAPI_KEY is required")

        self.api_key = api_key
        self.base_url = "https://newsapi.org/v2"

    async def search_multiple_sources(
        self, query: str, sources: Optional[List[str]] = None
    ) -> Dict:
        try:
            endpoint = f"{self.base_url}/everything"

            params = {
                "q": query,
                "apiKey": self.api_key,
                "language": "en",
                "sortBy": "relevancy",
                "pageSize": 20,
            }

            if sources:
                params["domains"] = ",".join(sources)

            response = requests.get(endpoint, params=params, timeout=10)
            data = response.json()

            if data.get("status") != "ok":
                raise Exception(
                    f"NewsAPI error: {data.get('message', 'Unknown error')}"
                )

            articles = []
            for article in data.get("articles", []):
                articles.append(
                    {
                        "title": article.get("title", ""),
                        "description": article.get("description", ""),
                        "url": article.get("url", ""),
                        "source": article.get("source", {}).get("name", "Unknown"),
                        "author": article.get("author", "Unknown"),
                        "publishedAt": article.get("publishedAt", ""),
                        "urlToImage": article.get("urlToImage", ""),
                    }
                )

            return {
                "query": query,
                "totalResults": data.get("totalResults", 0),
                "articles": articles,
            }

        except Exception as e:
            print(f"News search error: {str(e)}")
            return {"query": query, "totalResults": 0, "articles": [], "error": str(e)}

    async def find_similar(self, query: str, exclude_domain: str = "") -> List[Dict]:
        try:
            result = await self.search_multiple_sources(query)
            articles = result.get("articles", [])

            if exclude_domain:
                articles = [
                    a for a in articles if exclude_domain not in a.get("url", "")
                ]

            return articles[:5]

        except Exception as e:
            print(f"Find similar error: {str(e)}")
            return []
