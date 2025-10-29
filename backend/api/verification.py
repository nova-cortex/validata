from fastapi import HTTPException
from pydantic import HttpUrl
from typing import Dict, Any

from services.article_extractor import ArticleExtractor
from services.fact_checker import FactChecker
from services.news_searcher import NewsSearcher
from services.credibility_scorer import CredibilityScorer


from pydantic import BaseModel, HttpUrl


class URLVerificationRequest(BaseModel):
    url: HttpUrl


async def verify_article_handler(
    request: URLVerificationRequest,
    article_extractor: ArticleExtractor,
    fact_checker: FactChecker,
    news_searcher: NewsSearcher,
    credibility_scorer: CredibilityScorer,
) -> Dict[str, Any]:
    try:
        url = str(request.url)

        print(f"Extracting article from: {url}")
        article_data = article_extractor.extract(url)

        if not article_data or not article_data.get("text"):
            raise HTTPException(
                status_code=400, detail="Failed to extract article content"
            )

        print("Analyzing credibility...")
        credibility_data = await credibility_scorer.analyze(
            url=url,
            title=article_data.get("title", ""),
            text=article_data.get("text", ""),
            author=article_data.get("author", ""),
            publish_date=article_data.get("publish_date", ""),
        )

        print("Checking claims...")
        fact_check_results = await fact_checker.check_claims(
            text=article_data.get("text", ""), title=article_data.get("title", "")
        )

        print("Searching for similar articles...")
        similar_articles = await news_searcher.find_similar(
            query=article_data.get("title", ""), exclude_domain=url
        )

        return {
            "success": True,
            "article": {
                "title": article_data.get("title", ""),
                "author": article_data.get("author", ""),
                "publish_date": article_data.get("publish_date", ""),
                "summary": article_data.get("summary", ""),
                "text_preview": article_data.get("text", "")[:500] + "...",
                "top_image": article_data.get("top_image", ""),
            },
            "credibility": credibility_data,
            "fact_checks": fact_check_results,
            "similar_articles": similar_articles,
        }

    except Exception as e:
        print(f"Error in verify_article_handler: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
