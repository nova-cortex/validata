from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import HttpUrl, BaseModel
import os
from dotenv import load_dotenv

from services.article_extractor import ArticleExtractor
from services.fact_checker import FactChecker
from services.news_searcher import NewsSearcher
from services.credibility_scorer import CredibilityScorer

import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from api.verification import verify_article_handler, URLVerificationRequest
from api.search import search_news_handler, NewsSearchRequest

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

article_extractor = ArticleExtractor()
fact_checker = FactChecker(api_key=os.getenv("GEMINI_API_KEY"))
news_searcher = NewsSearcher(api_key=os.getenv("NEWSAPI_KEY"))
credibility_scorer = CredibilityScorer(api_key=os.getenv("GEMINI_API_KEY"))


@app.get("/")
def read_root():
    return {
        "message": "Fake News Detector API",
        "version": "1.0.0",
        "endpoints": {
            "verify_article": "/api/verify",
            "search_news": "/api/search",
            "health": "/health",
        },
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/api/verify")
async def verify_article(request: URLVerificationRequest):
    return await verify_article_handler(
        request, article_extractor, fact_checker, news_searcher, credibility_scorer
    )


@app.post("/api/search")
async def search_news(request: NewsSearchRequest):
    return await search_news_handler(
        request, fact_checker, news_searcher, credibility_scorer
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
