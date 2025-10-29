import requests
import os
from dotenv import load_dotenv
from typing import Dict, Any
import json

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")


def verify_article(url: str) -> Dict[str, Any]:
    try:
        if not url or not isinstance(url, str):
            return {"success": False, "detail": "Invalid URL provided"}

        url = url.strip()

        if not url.startswith(("http://", "https://")):
            return {
                "success": False,
                "detail": "URL must start with http:// or https://",
            }

        response = requests.post(
            f"{BACKEND_URL}/api/verify",
            json={"url": url},
            timeout=120,
        )

        if response.status_code == 422:
            try:
                error_data = response.json()
                detail = error_data.get("detail", "Invalid URL format")
                return {"success": False, "detail": f"URL validation failed: {detail}"}
            except json.JSONDecodeError:
                return {
                    "success": False,
                    "detail": "Invalid URL format. Please provide a complete news article URL.",
                }

        elif response.status_code == 400:
            try:
                error_data = response.json()
                return {
                    "success": False,
                    "detail": error_data.get("detail", "Bad request"),
                }
            except json.JSONDecodeError:
                return {
                    "success": False,
                    "detail": "Bad request. Please check your URL and try again.",
                }

        elif response.status_code == 500:
            try:
                error_data = response.json()
                return {
                    "success": False,
                    "detail": f"Server error: {error_data.get('detail', 'Internal server error')}",
                }
            except json.JSONDecodeError:
                return {
                    "success": False,
                    "detail": "Internal server error. Please try again later.",
                }

        elif response.status_code == 404:
            return {
                "success": False,
                "detail": "API endpoint not found. Please check if the backend server is running correctly.",
            }

        response.raise_for_status()

        return response.json()

    except requests.exceptions.Timeout:
        return {
            "success": False,
            "detail": "Request timed out after 120 seconds. The article may be too large or the server is busy. Please try again.",
        }
    except requests.exceptions.ConnectionError:
        return {
            "success": False,
            "detail": f"Cannot connect to backend server at {BACKEND_URL}. Please ensure the server is running.",
        }
    except requests.exceptions.HTTPError as e:
        return {"success": False, "detail": f"HTTP error occurred: {str(e)}"}
    except requests.exceptions.RequestException as e:
        return {"success": False, "detail": f"Request error: {str(e)}"}
    except json.JSONDecodeError:
        return {
            "success": False,
            "detail": "Failed to parse server response. The server may have returned invalid data.",
        }
    except Exception as e:
        return {"success": False, "detail": f"Unexpected error: {str(e)}"}


def search_news(query: str) -> Dict[str, Any]:
    try:
        if not query or not isinstance(query, str):
            return {"success": False, "detail": "Invalid search query provided"}

        query = query.strip()

        if len(query) < 3:
            return {
                "success": False,
                "detail": "Search query must be at least 3 characters long",
            }

        if len(query) > 200:
            return {
                "success": False,
                "detail": "Search query is too long (maximum 200 characters)",
            }

        response = requests.post(
            f"{BACKEND_URL}/api/search",
            json={"query": query},
            timeout=120,
        )

        if response.status_code == 422:
            try:
                error_data = response.json()
                detail = error_data.get("detail", "Invalid query format")
                return {
                    "success": False,
                    "detail": f"Query validation failed: {detail}",
                }
            except json.JSONDecodeError:
                return {
                    "success": False,
                    "detail": "Invalid query format. Please provide a valid search query.",
                }

        elif response.status_code == 400:
            try:
                error_data = response.json()
                return {
                    "success": False,
                    "detail": error_data.get("detail", "Bad request"),
                }
            except json.JSONDecodeError:
                return {
                    "success": False,
                    "detail": "Bad request. Please check your query and try again.",
                }

        elif response.status_code == 500:
            try:
                error_data = response.json()
                return {
                    "success": False,
                    "detail": f"Server error: {error_data.get('detail', 'Internal server error')}",
                }
            except json.JSONDecodeError:
                return {
                    "success": False,
                    "detail": "Internal server error. Please try again later.",
                }

        elif response.status_code == 404:
            return {
                "success": False,
                "detail": "API endpoint not found. Please check if the backend server is running correctly.",
            }

        response.raise_for_status()

        return response.json()

    except requests.exceptions.Timeout:
        return {
            "success": False,
            "detail": "Request timed out after 120 seconds. Please try again with a more specific query.",
        }
    except requests.exceptions.ConnectionError:
        return {
            "success": False,
            "detail": f"Cannot connect to backend server at {BACKEND_URL}. Please ensure the server is running.",
        }
    except requests.exceptions.HTTPError as e:
        return {"success": False, "detail": f"HTTP error occurred: {str(e)}"}
    except requests.exceptions.RequestException as e:
        return {"success": False, "detail": f"Request error: {str(e)}"}
    except json.JSONDecodeError:
        return {
            "success": False,
            "detail": "Failed to parse server response. The server may have returned invalid data.",
        }
    except Exception as e:
        return {"success": False, "detail": f"Unexpected error: {str(e)}"}


def check_backend_health() -> Dict[str, Any]:
    try:
        response = requests.get(
            f"{BACKEND_URL}/health",
            timeout=5,
        )

        if response.status_code == 200:
            return {
                "success": True,
                "status": "healthy",
                "message": "Backend server is running",
            }
        else:
            return {
                "success": False,
                "status": "unhealthy",
                "message": f"Backend returned status code {response.status_code}",
            }

    except requests.exceptions.ConnectionError:
        return {
            "success": False,
            "status": "offline",
            "message": f"Cannot connect to backend at {BACKEND_URL}",
        }
    except requests.exceptions.Timeout:
        return {
            "success": False,
            "status": "timeout",
            "message": "Backend health check timed out",
        }
    except Exception as e:
        return {
            "success": False,
            "status": "error",
            "message": f"Health check failed: {str(e)}",
        }
