# Usage Guide for Validata: AI-Powered Fake News Detector

A comprehensive guide on how to set up, run, and interact with the Validata application for AI-powered news verification and multi-source analysis.

## Table of Contents

- [Overview](#overview)
- [Quick Start](#quick-start)
- [Step-by-Step Setup](#step-by-step-setup)
- [Application Modes](#application-modes)
- [Troubleshooting](#troubleshooting)
- [Best Practices](#best-practices)

## Overview

Validata is an AI-powered tool designed to help users combat misinformation by providing comprehensive analysis of news articles and topics. It leverages Google Gemini for credibility scoring and fact-checking, and NewsAPI for multi-source comparison.

Key functionalities include:
- **Article URL Verification**: Analyze a single news article for credibility, claims, and bias.
- **News Topic Search**: Get a neutral summary and source diversity analysis for a given news topic from multiple sources.
- **Interactive Streamlit Frontend**: A user-friendly interface for seamless interaction.

## Quick Start

Follow these steps to get Validata up and running quickly:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nova-cortex/validata.git
   cd validata
   ```

2. **Set up environment variables:**
   Create a `.env` file in the root directory and add your API keys:
   ```
   GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
   NEWSAPI_KEY="YOUR_NEWSAPI_KEY"
   BACKEND_URL="http://localhost:8000" # Default, change if your backend runs on a different host/port
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the Backend Server:**
   Open a terminal, navigate to the `backend` directory, and run:
   ```bash
   cd backend
   python app.py
   ```
   You should see output indicating Uvicorn running on `http://0.0.0.0:8000`.

5. **Start the Frontend Application:**
   Open a **new** terminal, navigate to the `frontend` directory, and run:
   ```bash
   cd frontend
   streamlit run app.py
   ```
   This will open the Validata application in your web browser, usually at `http://localhost:8501`.

## Step-by-Step Setup

### 1. Prerequisites

Ensure you have the following installed:
- **Python 3.8+**: Download from [python.org](https://www.python.org/downloads/)
- **pip**: Usually comes with Python. Verify with `pip --version`.
- **API Keys**:
    - **Google Gemini API Key**: Obtain from [Google AI Studio](https://aistudio.google.com/app/apikey).
    - **NewsAPI Key**: Obtain from [newsapi.org](https://newsapi.org/register).

### 2. Clone the Repository

```bash
git clone https://github.com/nova-cortex/validata.git
cd validata
```

### 3. Configure Environment Variables

Create a file named `.env` in the root directory of the `validata` project.
Add your API keys and backend URL to this file:

```dotenv
GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"
NEWSAPI_KEY="YOUR_NEWSAPI_KEY_HERE"
BACKEND_URL="http://localhost:8000"
```
**Important**: Replace `"YOUR_GEMINI_API_KEY_HERE"` and `"YOUR_NEWSAPI_KEY_HERE"` with your actual API keys. Do not share your `.env` file or API keys publicly.

### 4. Install Dependencies

#### All Dependencies
Navigate to the root directory of the project and install:
```bash
pip install -r requirements.txt
```

### 5. Run the Backend Server

The backend provides the AI-powered analysis services. It must be running for the frontend to function.

Open a **new terminal** (or keep the current one if you're done with installations) and navigate to the `backend` directory:
```bash
cd backend
```
Activate your Python virtual environment if you're using one (recommended):
```bash
# On Windows
.\env\Scripts\activate
# On macOS/Linux
source env/bin/activate
```
Then, start the FastAPI application:
```bash
python app.py
```
You should see output similar to this, indicating the server is running:
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [PID]
INFO:     Started server process [PID]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
You can verify the backend is accessible by opening `http://localhost:8000` in your web browser. You should see a JSON response with API endpoints.

### 6. Run the Frontend Application

The frontend is a Streamlit application that provides the user interface.

Open **another new terminal** and navigate to the `frontend` directory:
```bash
cd frontend
```
Activate your Python virtual environment if you're using one:
```bash
# On Windows
.\env\Scripts\activate
# On macOS/Linux
source env/bin/activate
```
Then, start the Streamlit application:
```bash
streamlit run app.py
```
This command will automatically open the Validata application in your default web browser, typically at `http://localhost:8501`.

## Application Modes

Validata offers two primary modes of operation, accessible via the sidebar in the Streamlit application:

### 🔗 Verify Article URL

This mode allows you to analyze a single news article for its credibility.

1. **Paste a URL**: Enter the complete URL of a news article (e.g., `https://www.bbc.com/news/example-article`).
2. **Click "Verify Article"**: The application will:
   - Extract the article content.
   - Analyze its credibility using Google Gemini (scoring source reputation, writing quality, evidence, objectivity, transparency).
   - Fact-check key claims.
   - Search for similar articles from other sources for comparison.
   - Detect potential manipulation tactics and political bias.
3. **Review Results**: The results will be displayed, including an overall credibility score, detailed analysis, fact-check findings, and links to similar articles.

**Tips for Article Verification:**
- Use complete URLs (starting with `http://` or `https://`).
- Prefer articles from well-known news sources for better analysis.
- Be aware that some paywalled or heavily JavaScript-driven sites may not be fully extractable.

### 🔍 Search News Topic

This mode allows you to get a multi-source analysis for a given news topic or question.

1. **Enter a Query**: Type a news topic or question (e.g., "climate change summit results", "AI developments 2025").
2. **Click "Search News"**: The application will:
   - Search multiple news sources using NewsAPI for relevant articles.
   - Generate a neutral consensus summary of the findings.
   - Identify points of agreement and disagreement across sources.
   - Analyze the diversity of sources found.
3. **Review Results**: The results will include a neutral summary, lists of agreements and disagreements, source distribution charts, and a list of all found articles.

**Tips for News Topic Search:**
- Use clear and specific queries for better results.
- Broaden your search if no articles are found.
- Pay attention to the "Source Diversity" score to gauge the breadth of perspectives.

## Troubleshooting

### Backend Server Not Connected

**Problem**: The frontend shows a "Backend Server Not Connected" error.
**Solution**:
1. Ensure the backend server is running. Navigate to the `backend` directory in a terminal and run `python app.py`.
2. Check if the backend is running on `http://localhost:8000`. If not, update the `BACKEND_URL` in your `.env` file.
3. Verify that port 8000 is not blocked by a firewall or used by another application.

### Request Timed Out

**Problem**: Analysis takes too long and results in a timeout error.
**Solution**:
- **For Article Verification**: The article might be very long, the source website slow, or AI analysis is taking longer. Try a shorter article or a different source.
- **For News Search**: The query might be too broad, leading to extensive searches. Try a more specific query.
- Check your internet connection.

### Invalid URL Format

**Problem**: The URL provided is not recognized as valid.
**Solution**:
- Ensure the URL starts with `http://` or `https://`.
- Make sure it includes a valid domain (e.g., `example.com`).
- Do not enter file paths or commands.

### No Articles Found (News Search)

**Problem**: Your news search query returns no articles.
**Solution**:
- Broaden your search query.
- Try different keywords.
- Check for typos.
- NewsAPI primarily covers recent articles; try searching for current events.

### API Rate Limit Reached

**Problem**: You receive an error indicating an API rate limit.
**Solution**:
- Wait a few minutes and try again. API limits usually reset after a short period.
- If you are a developer, check your API usage dashboards for Google Gemini and NewsAPI. Consider upgrading your API plan if you hit limits frequently.

### Cannot Extract Article Content

**Problem**: The application fails to extract content from a given URL.
**Solution**:
- The article might be behind a paywall or require a subscription.
- The website might have strong anti-bot protection.
- The content might be dynamically loaded via JavaScript, which `Newspaper3k` might struggle with.
- Try articles from mainstream news sites like BBC, Reuters, AP News, The Guardian, or NPR.

## Best Practices

- **Always Cross-Reference**: Use Validata's multi-source comparison feature to get a balanced view.
- **Be Critical**: Even with AI analysis, always apply your own critical thinking.
- **Check Sources**: Pay attention to the source reputation and diversity.
- **Understand Bias**: Recognize that all news sources may have some level of bias.
- **Review Claims**: Look at the fact-check results and the reasoning provided.
- **Keep API Keys Secure**: Never commit your `.env` file to a public repository.

---

**Made with ❤️ for the developer community**

*Validata helps users navigate the complex news landscape with AI-powered insights.*
