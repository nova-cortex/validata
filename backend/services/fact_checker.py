import google.generativeai as genai
from typing import Dict, List
import json


class FactChecker:
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("GEMINI_API_KEY is required")

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    async def check_claims(self, text: str, title: str = "") -> Dict:
        try:
            text_sample = text[:3000]

            prompt = f"""
Analyze the following news article excerpt to identify key factual claims and assess their verifiability.

Title: {title}
Article Text:
{text_sample}

1. Identify up to 5 main factual claims made in the text.
2. For each claim, determine its verifiability (e.g., "Verifiable", "Partially Verifiable", "Difficult to Verify").
3. Provide brief reasoning for your verifiability assessment.
4. Identify any potential manipulation tactics used (e.g., "Emotional Language", "Misleading Statistics", "Appeal to Authority").

Return the result in a clean JSON format:
{{
    "claims": [
        {{
            "claim": "The specific claim made in the article.",
            "verifiability": "Verifiable/Partially Verifiable/Difficult to Verify",
            "reasoning": "Brief explanation of why."
        }}
    ],
    "manipulation_tactics": ["tactic 1", "tactic 2"]
}}
"""
            response = self.model.generate_content(prompt)
            result_text = response.text

            try:
                if "```json" in result_text:
                    result_text = result_text.split("```json")[1].split("```")[0]
                elif "```" in result_text:
                    result_text = result_text.split("```")[1].split("```")[0]

                return json.loads(result_text.strip())

            except (json.JSONDecodeError, IndexError):
                return {
                    "claims": [],
                    "manipulation_tactics": ["Failed to parse AI model response"],
                }

        except Exception as e:
            print(f"Claim verification error: {str(e)}")
            return {
                "claims": [],
                "manipulation_tactics": [f"An error occurred: {str(e)}"],
            }

    async def generate_neutral_summary(self, articles: List[Dict], query: str) -> Dict:
        try:
            if not articles:
                return {
                    "consensus_summary": "Not enough articles to generate a summary.",
                    "points_of_agreement": [],
                    "points_of_disagreement": [],
                }

            article_summaries = "\n\n".join(
                [
                    f"Source: {a.get('source', 'Unknown')}\nTitle: {a.get('title', '')}\n"
                    f"Summary: {a.get('description', '')}"
                    for a in articles[:5]
                ]
            )

            prompt = f"""
Analyze the following article summaries on the topic of "{query}".

Summaries:
{article_summaries}

Based on these summaries:
1. Write a neutral, balanced consensus summary of the key events or findings.
2. List the main points of agreement across the different sources.
3. List the main points of disagreement or different perspectives.
4. Provide a media literacy tip relevant to the topic.

Return the result in a clean JSON format:
{{
    "consensus_summary": "Your neutral summary here.",
    "points_of_agreement": ["Point 1", "Point 2"],
    "points_of_disagreement": ["Point A", "Point B"],
    "media_literacy_tip": "Your tip here."
}}
"""
            response = self.model.generate_content(prompt)
            result_text = response.text

            try:
                if "```json" in result_text:
                    result_text = result_text.split("```json")[1].split("```")[0]
                elif "```" in result_text:
                    result_text = result_text.split("```")[1].split("```")[0]

                return json.loads(result_text.strip())

            except (json.JSONDecodeError, IndexError):
                return {
                    "consensus_summary": "Could not parse the generated summary.",
                    "points_of_agreement": [],
                    "points_of_disagreement": [],
                    "media_literacy_tip": "Always be critical of sources.",
                }

        except Exception as e:
            print(f"Neutral summary error: {str(e)}")
            return {
                "consensus_summary": f"An error occurred: {str(e)}",
                "points_of_agreement": [],
                "points_of_disagreement": [],
                "media_literacy_tip": "Check for errors in your tools.",
            }
