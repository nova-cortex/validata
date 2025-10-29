from typing import Dict, Any
import re
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


def clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^\w\s.,!?-]", "", text)
    return text.strip()


def truncate_text(text: str, max_length: int = 500) -> str:
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."


def format_score(score: int) -> Dict[str, Any]:
    if score >= 80:
        return {"score": score, "label": "Highly Credible", "color": "green"}
    elif score >= 60:
        return {"score": score, "label": "Moderately Credible", "color": "yellow"}
    elif score >= 40:
        return {"score": score, "label": "Low Credibility", "color": "orange"}
    else:
        return {"score": score, "label": "Very Low Credibility", "color": "red"}
