import streamlit as st
from styles import apply_custom_styles
from display import display_article_verification, display_news_search_results
from api_client import verify_article, search_news
from error_components import (
    show_connection_error,
    show_timeout_error,
    show_invalid_url_error,
    show_extraction_failed_error,
    show_api_rate_limit_error,
    show_success_message,
)
import re
from urllib.parse import urlparse

st.set_page_config(
    page_title="Validata",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_custom_styles()

if "url_value" not in st.session_state:
    st.session_state.url_value = ""
if "query_value" not in st.session_state:
    st.session_state.query_value = ""


def is_valid_url(url: str) -> tuple[bool, str]:
    if not url or url.strip() == "":
        return False, "URL cannot be empty"

    invalid_patterns = [
        r"^env/",
        r"Scripts/",
        r"^[A-Z]:\\",
        r"^/",
        r"activate$",
        r"\.py$",
        r"\.exe$",
    ]

    for pattern in invalid_patterns:
        if re.search(pattern, url):
            return False, "This appears to be a file path or command, not a URL"

    try:
        result = urlparse(url)
        if not all([result.scheme, result.netloc]):
            return False, "URL must include http:// or https:// and a domain name"

        if result.scheme not in ["http", "https"]:
            return False, "URL must start with http:// or https://"

        if "." not in result.netloc:
            return False, "URL must contain a valid domain (e.g., example.com)"

        return True, ""
    except Exception as e:
        return False, f"Invalid URL format: {str(e)}"


def is_valid_query(query: str) -> tuple[bool, str]:
    if not query or query.strip() == "":
        return False, "Search query cannot be empty"

    invalid_patterns = [
        r"^env/",
        r"Scripts/",
        r"^[A-Z]:\\",
        r"activate$",
        r"\.py$",
        r"\.exe$",
        r"http://",
        r"https://",
    ]

    for pattern in invalid_patterns:
        if re.search(pattern, query):
            return (
                False,
                "This appears to be a file path, command, or URL. Please enter a news topic or question instead.",
            )

    if len(query.strip()) < 3:
        return False, "Search query must be at least 3 characters long"

    if len(query) > 200:
        return False, "Search query is too long (maximum 200 characters)"

    return True, ""


def show_error(message: str, details: str = None):
    st.error(f"❌ **Error:** {message}")
    if details:
        with st.expander("🔍 More Details"):
            st.code(details, language="text")


def show_warning(message: str):
    st.warning(f"⚠️ **Warning:** {message}")


def show_success(message: str):
    st.success(f"✅ {message}")


def render_header():
    st.markdown('<h1 class="main-header">🔍 VALIDATA</h1>', unsafe_allow_html=True)
    st.markdown(
        '<p class="sub-header">AI-Powered News Verification · Multi-Source Analysis · Real-Time Fact Checking</p>',
        unsafe_allow_html=True,
    )


def render_sidebar():
    with st.sidebar:
        st.markdown("## 🎯 Choose Your Action")
        st.markdown("Select how you'd like to analyze news content")

        mode = st.radio(
            "Select Mode:",
            ["🔗 Verify Article URL", "🔍 Search News Topic"],
            label_visibility="collapsed",
        )

        st.markdown("---")

        st.markdown("### ℹ️ About This Tool")
        st.markdown(
            """
            <div style='background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%); 
                        padding: 1rem; 
                        border-radius: 12px; 
                        border-left: 4px solid #667eea;
                        margin: 1rem 0;'>
                <p style='margin: 0; color: #e0e0e0; line-height: 1.6;'>
                    <strong>Comprehensive Analysis:</strong><br>
                    ✓ Credibility scoring with AI<br>
                    ✓ Automated fact-checking<br>
                    ✓ Multi-source comparison<br>
                    ✓ Bias & manipulation detection
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("---")

        st.markdown("### 🛠️ Technology Stack")
        col1, col2 = st.columns([1, 3])

        with col2:
            st.markdown(
                """
                <div style='font-size: 0.9rem; color: #b0b0b0;'>
                    <p style='margin: 0.3rem 0;'>🤖 <strong>Google Gemini 2.5</strong></p>
                    <p style='margin: 0.3rem 0;'>📰 <strong>NewsAPI</strong></p>
                    <p style='margin: 0.3rem 0;'>📄 <strong>Newspaper3k</strong></p>
                    <p style='margin: 0.3rem 0;'>📊 <strong>Plotly Charts</strong></p>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("---")

        with st.expander("💡 Pro Tips"):
            st.markdown(
                """
                **For Best Results:**
                - Use complete article URLs with http:// or https://
                - Provide clear, specific search queries
                - Check multiple sources
                - Review the detailed analysis
                - Cross-reference claims
                - Consider source reputation
                """
            )

        return mode


def render_verify_mode():
    st.markdown("## 🔗 Article Verification")

    st.markdown(
        """
        <div style='background: linear-gradient(135deg, rgba(15, 52, 96, 0.95) 0%, rgba(22, 33, 62, 0.95) 100%); 
                    padding: 1.5rem; 
                    border-radius: 12px; 
                    margin-bottom: 2rem;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.3);
                    border: 1px solid #533483;'>
            <p style='color: #e0e0e0; margin: 0; line-height: 1.6;'>
                Paste a news article URL below for comprehensive AI-powered analysis. 
                We'll extract content, verify claims, assess credibility, and find similar 
                articles from other sources for comparison.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style='background: rgba(102, 126, 234, 0.1); 
                    padding: 0.75rem 1rem; 
                    border-radius: 8px; 
                    margin-bottom: 1rem;
                    border-left: 3px solid #667eea;'>
            <small style='color: #b0b0b0;'>
                <strong>✓ Valid:</strong> https://www.bbc.com/news/article-name<br>
                <strong>✗ Invalid:</strong> File paths, commands, or incomplete URLs
            </small>
        </div>
        """,
        unsafe_allow_html=True,
    )

    url_input = st.text_input(
        "Enter Article URL:",
        value=st.session_state.url_value,
        placeholder="https://example.com/news-article",
        help="Paste the complete URL of the news article you want to verify",
        key="url_input",
    )

    col1, col2, col3, col4 = st.columns([1.5, 1, 1, 2.5])

    with col1:
        verify_button = st.button(
            "🔍 Verify Article", type="primary", use_container_width=True
        )

    with col2:
        if st.button("🔄 Clear", use_container_width=True, key="clear_url"):
            st.session_state.url_value = ""
            st.rerun()

    if verify_button:
        if not url_input or url_input.strip() == "":
            show_error("Please enter a URL to verify")
        else:
            is_valid, error_msg = is_valid_url(url_input.strip())

            if not is_valid:
                show_invalid_url_error(url_input.strip())
            else:
                try:
                    with st.spinner(
                        "🔄 Analyzing article... This may take 30-60 seconds..."
                    ):
                        progress_bar = st.progress(0)
                        status_text = st.empty()

                        status_text.text("⏳ Extracting article content...")
                        progress_bar.progress(25)

                        data = verify_article(url_input.strip())

                        progress_bar.progress(50)
                        status_text.text("⏳ Analyzing credibility...")

                        if data.get("success"):
                            status_text.text("✅ Analysis complete!")
                            progress_bar.progress(100)

                            import time

                            time.sleep(0.5)
                            progress_bar.empty()
                            status_text.empty()

                            show_success_message(
                                "Article verification completed successfully!"
                            )
                            display_article_verification(data)
                        else:
                            progress_bar.empty()
                            status_text.empty()

                            error_detail = data.get("detail", "Unknown error occurred")

                            if "connect" in error_detail.lower():
                                show_connection_error()
                            elif "timeout" in error_detail.lower():
                                show_timeout_error("article verification")
                            elif "extract" in error_detail.lower():
                                show_extraction_failed_error()
                            elif (
                                "422" in error_detail
                                or "unprocessable" in error_detail.lower()
                            ):
                                show_invalid_url_error(url_input.strip())
                            elif (
                                "rate" in error_detail.lower()
                                or "limit" in error_detail.lower()
                            ):
                                show_api_rate_limit_error()
                            else:
                                show_error(
                                    "Failed to verify article",
                                    f"Error details: {error_detail}\n\n"
                                    + "Please try again or contact support if the issue persists.",
                                )

                except Exception as e:
                    show_error(
                        "An unexpected error occurred",
                        f"Error type: {type(e).__name__}\n"
                        + f"Error message: {str(e)}\n\n"
                        + "Please try again or contact support if the issue persists.",
                    )

    with st.expander("💡 Try These Example URLs", expanded=False):
        st.markdown("**High-Credibility Sources:**")
        example_urls = [
            ("BBC News", "https://www.bbc.com/news/world"),
            ("Reuters", "https://www.reuters.com/world/"),
            ("Associated Press", "https://apnews.com/"),
        ]

        for name, url in example_urls:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.code(url, language=None)
            with col2:
                if st.button(f"Use", key=f"example_{name}"):
                    st.session_state.url_value = url
                    st.rerun()


def render_search_mode():
    st.markdown("## 🔍 News Topic Search")

    st.markdown(
        """
        <div style='background: linear-gradient(135deg, rgba(15, 52, 96, 0.95) 0%, rgba(22, 33, 62, 0.95) 100%); 
                    padding: 1.5rem; 
                    border-radius: 12px; 
                    margin-bottom: 2rem;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.3);
                    border: 1px solid #533483;'>
            <p style='color: #e0e0e0; margin: 0; line-height: 1.6;'>
                Search for any news topic to get a comprehensive analysis from multiple sources. 
                Our AI will generate a neutral summary, identify points of agreement and disagreement, 
                and analyze source diversity.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style='background: rgba(102, 126, 234, 0.1); 
                    padding: 0.75rem 1rem; 
                    border-radius: 8px; 
                    margin-bottom: 1rem;
                    border-left: 3px solid #667eea;'>
            <small style='color: #b0b0b0;'>
                <strong>✓ Valid:</strong> "climate change summit results", "AI developments 2025"<br>
                <strong>✗ Invalid:</strong> URLs, file paths, or commands
            </small>
        </div>
        """,
        unsafe_allow_html=True,
    )

    query_input = st.text_input(
        "Enter Your Question or Topic:",
        value=st.session_state.query_value,
        placeholder="What happened with the recent climate summit?",
        help="Enter a news topic or question to search multiple sources",
        key="query_input",
    )

    col1, col2, col3, col4 = st.columns([1.5, 1, 1, 2.5])

    with col1:
        search_button = st.button(
            "🔍 Search News", type="primary", use_container_width=True
        )

    with col2:
        if st.button("🔄 Clear", use_container_width=True, key="clear_search"):
            st.session_state.query_value = ""
            st.rerun()

    if search_button:
        if not query_input or query_input.strip() == "":
            show_error("Please enter a search query")
        else:
            is_valid, error_msg = is_valid_query(query_input.strip())

            if not is_valid:
                show_error(
                    error_msg,
                    f"You entered: {query_input}\n\nPlease provide a clear news topic or question instead.",
                )
            else:
                try:
                    with st.spinner(
                        "🔄 Searching multiple sources... This may take 30-60 seconds..."
                    ):
                        progress_bar = st.progress(0)
                        status_text = st.empty()

                        status_text.text("⏳ Searching news sources...")
                        progress_bar.progress(25)

                        data = search_news(query_input.strip())

                        progress_bar.progress(50)
                        status_text.text("⏳ Generating analysis...")

                        if data.get("success"):
                            status_text.text("✅ Search complete!")
                            progress_bar.progress(100)

                            import time

                            time.sleep(0.5)
                            progress_bar.empty()
                            status_text.empty()

                            articles = data.get("articles", [])
                            if not articles or len(articles) == 0:
                                from error_components import show_no_results_error

                                show_no_results_error(query_input.strip())
                            else:
                                show_success_message(
                                    f"Found {len(articles)} articles from multiple sources!",
                                    "🎉",
                                )
                                display_news_search_results(data)
                        else:
                            progress_bar.empty()
                            status_text.empty()

                            error_detail = data.get("detail", "Unknown error occurred")

                            if "connect" in error_detail.lower():
                                show_connection_error()
                            elif "timeout" in error_detail.lower():
                                show_timeout_error("news search")
                            elif (
                                "newsapi" in error_detail.lower()
                                or "api" in error_detail.lower()
                            ):
                                show_api_rate_limit_error()
                            else:
                                show_error(
                                    "Failed to search news",
                                    f"Error details: {error_detail}\n\n"
                                    + "Please try again or contact support if the issue persists.",
                                )

                except Exception as e:
                    show_error(
                        "An unexpected error occurred",
                        f"Error type: {type(e).__name__}\n"
                        + f"Error message: {str(e)}\n\n"
                        + "Please try again or contact support if the issue persists.",
                    )

    with st.expander("💡 Try These Example Searches", expanded=False):
        st.markdown("**Popular Topics:**")
        example_queries = [
            "Latest developments in artificial intelligence",
            "Climate change summit results",
            "Recent economic policy changes",
            "Space exploration updates",
            "Global health initiatives",
        ]

        for i, query in enumerate(example_queries):
            col1, col2 = st.columns([4, 1])
            with col1:
                st.markdown(f"• {query}")
            with col2:
                if st.button("Use", key=f"query_{i}"):
                    st.session_state.query_value = query
                    st.rerun()


def main():
    render_header()
    mode = render_sidebar()

    if "🔗 Verify" in mode:
        render_verify_mode()
    else:
        render_search_mode()


if __name__ == "__main__":
    main()
