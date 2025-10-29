from fastapi import HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any, Optional

from services.fact_checker import FactChecker
from services.news_searcher import NewsSearcher
from services.credibility_scorer import CredibilityScorer


class NewsSearchRequest(BaseModel):
    query: str
    sources: Optional[List[str]] = None


async def search_news_handler(
    request: NewsSearchRequest,
    fact_checker: FactChecker,
    news_searcher: NewsSearcher,
    credibility_scorer: CredibilityScorer,
) -> Dict[str, Any]:
    try:
        query = request.query

        print(f"Searching news for: {query}")
        search_results = await news_searcher.search_multiple_sources(
            query=query, sources=request.sources
        )

        if not search_results or len(search_results.get("articles", [])) == 0:
            return {
                "success": False,
                "message": "No articles found for the given query",
            }

        print("Generating neutral summary...")
        summary_data = await fact_checker.generate_neutral_summary(
            articles=search_results.get("articles", []), query=query
        )

        print("Analyzing bias distribution...")
        bias_analysis = credibility_scorer.analyze_bias_distribution(
            articles=search_results.get("articles", [])
        )

        return {
            "success": True,
            "query": query,
            "summary": summary_data,
            "articles": search_results.get("articles", []),
            "bias_analysis": bias_analysis,
            "total_sources": len(search_results.get("articles", [])),
        }

    except Exception as e:
        print(f"Error in search_news_handler: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
