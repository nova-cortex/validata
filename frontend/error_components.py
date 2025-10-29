import streamlit as st


def show_connection_error():
    st.markdown(
        """
        <div style='background: linear-gradient(135deg, rgba(244, 67, 54, 0.2) 0%, rgba(229, 57, 53, 0.2) 100%);
                    padding: 2rem;
                    border-radius: 16px;
                    border: 2px solid #f44336;
                    margin: 2rem 0;
                    text-align: center;'>
            <div style='font-size: 4rem; margin-bottom: 1rem;'>🔌</div>
            <h2 style='color: #ffffff; margin-bottom: 1rem;'>Backend Server Not Connected</h2>
            <p style='color: #e0e0e0; font-size: 1.1rem; line-height: 1.6;'>
                The application cannot connect to the backend server.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.expander("🔧 How to Fix This", expanded=True):
        st.markdown(
            """
            ### Step-by-Step Solution:
            
            **1. Start the Backend Server**
            ```bash
            cd backend
            env\\Scripts\\activate
            python app.py
            ```
            
            **2. Verify Server is Running**
            - You should see: `Uvicorn running on http://0.0.0.0:8000`
            - Open browser and visit: http://localhost:8000
            - You should see the API welcome message
            
            **3. Check Environment Variables**
            - Ensure `.env` file exists with API keys:
              - `GEMINI_API_KEY`
              - `NEWSAPI_KEY`
            
            **4. Verify Port Availability**
            - Make sure port 8000 is not being used by another application
            
            **Still having issues?**
            - Check firewall settings
            - Restart both frontend and backend
            - Check the backend terminal for error messages
            """
        )


def show_timeout_error(operation: str = "operation"):
    st.markdown(
        f"""
        <div style='background: linear-gradient(135deg, rgba(255, 152, 0, 0.2) 0%, rgba(245, 124, 0, 0.2) 100%);
                    padding: 2rem;
                    border-radius: 16px;
                    border: 2px solid #ff9800;
                    margin: 2rem 0;
                    text-align: center;'>
            <div style='font-size: 4rem; margin-bottom: 1rem;'>⏱️</div>
            <h2 style='color: #ffffff; margin-bottom: 1rem;'>Request Timed Out</h2>
            <p style='color: #e0e0e0; font-size: 1.1rem; line-height: 1.6;'>
                The {operation} took too long to complete (over 2 minutes).
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        ### 🤔 Why did this happen?
        
        - **Large Article**: The article might be very long
        - **Slow Website**: The source website is responding slowly
        - **Heavy Load**: The AI analysis is taking longer than usual
        - **Network Issues**: Poor internet connection
        
        ### 💡 What you can try:
        
        1. **Wait and retry** - Sometimes it works on the second attempt
        2. **Try a shorter article** - Smaller articles process faster
        3. **Check your internet** - Ensure stable connection
        4. **Try a different source** - Some websites load faster
        """
    )


def show_invalid_url_error(url: str):
    st.markdown(
        """
        <div style='background: linear-gradient(135deg, rgba(244, 67, 54, 0.2) 0%, rgba(229, 57, 53, 0.2) 100%);
                    padding: 2rem;
                    border-radius: 16px;
                    border: 2px solid #f44336;
                    margin: 2rem 0;
                    text-align: center;'>
            <div style='font-size: 4rem; margin-bottom: 1rem;'>🚫</div>
            <h2 style='color: #ffffff; margin-bottom: 1rem;'>Invalid URL Format</h2>
            <p style='color: #e0e0e0; font-size: 1.1rem; line-height: 1.6;'>
                The URL you provided is not in the correct format.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.code(f"You entered: {url}", language=None)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            ### ✅ Valid URLs:
            ```
            https://www.bbc.com/news/article
            http://example.com/story
            https://news.site.org/2025/article
            ```
            
            **Requirements:**
            - Must start with `http://` or `https://`
            - Must have a domain name (.com, .org, etc.)
            - Should point to a news article
            """
        )

    with col2:
        st.markdown(
            """
            ### ❌ Invalid Examples:
            ```
            www.example.com (missing http://)
            example.com/article (missing protocol)
            C:\\Users\\file.txt (file path)
            env/Scripts/activate (command)
            ```
            
            **Common Mistakes:**
            - Missing `http://` or `https://`
            - Entering file paths
            - Copying commands instead of URLs
            """
        )


def show_no_results_error(query: str):
    st.markdown(
        """
        <div style='background: linear-gradient(135deg, rgba(33, 150, 243, 0.2) 0%, rgba(21, 101, 192, 0.2) 100%);
                    padding: 2rem;
                    border-radius: 16px;
                    border: 2px solid #2196f3;
                    margin: 2rem 0;
                    text-align: center;'>
            <div style='font-size: 4rem; margin-bottom: 1rem;'>🔍</div>
            <h2 style='color: #ffffff; margin-bottom: 1rem;'>No Articles Found</h2>
            <p style='color: #e0e0e0; font-size: 1.1rem; line-height: 1.6;'>
                We couldn't find any articles matching your search.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.code(f"Your search: {query}", language=None)

    st.markdown(
        """
        ### 💡 Try these tips:
        
        **1. Broaden your search**
        - Instead of: "specific company quarterly earnings Q3 2025"
        - Try: "company earnings 2025"
        
        **2. Use different keywords**
        - Instead of: "utilization of renewable energy"
        - Try: "renewable energy usage" or "clean energy"
        
        **3. Check for typos**
        - Make sure words are spelled correctly
        
        **4. Be more general**
        - Instead of: "John Smith elected mayor of Springfield"
        - Try: "Springfield mayoral election"
        
        **5. Use recent topics**
        - News APIs typically have recent articles
        - Try searching for current events
        """
    )


def show_api_rate_limit_error():
    st.markdown(
        """
        <div style='background: linear-gradient(135deg, rgba(255, 152, 0, 0.2) 0%, rgba(245, 124, 0, 0.2) 100%);
                    padding: 2rem;
                    border-radius: 16px;
                    border: 2px solid #ff9800;
                    margin: 2rem 0;
                    text-align: center;'>
            <div style='font-size: 4rem; margin-bottom: 1rem;'>⚠️</div>
            <h2 style='color: #ffffff; margin-bottom: 1rem;'>API Rate Limit Reached</h2>
            <p style='color: #e0e0e0; font-size: 1.1rem; line-height: 1.6;'>
                You've made too many requests in a short time.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        ### ⏰ What to do:
        
        **Wait a bit**
        - Most API limits reset after a few minutes
        - Try again in 5-10 minutes
        
        **For developers:**
        - Check your API key limits on the provider dashboard
        - Consider upgrading your API plan if needed
        - NewsAPI free tier: 100 requests/day
        - Gemini API: Check your quota at https://makersuite.google.com/
        
        ### 📊 Current Usage:
        - If you're the developer, check the backend logs
        - Monitor your API usage on provider dashboards
        """
    )


def show_extraction_failed_error():
    st.markdown(
        """
        <div style='background: linear-gradient(135deg, rgba(244, 67, 54, 0.2) 0%, rgba(229, 57, 53, 0.2) 100%);
                    padding: 2rem;
                    border-radius: 16px;
                    border: 2px solid #f44336;
                    margin: 2rem 0;
                    text-align: center;'>
            <div style='font-size: 4rem; margin-bottom: 1rem;'>📄</div>
            <h2 style='color: #ffffff; margin-bottom: 1rem;'>Cannot Extract Article Content</h2>
            <p style='color: #e0e0e0; font-size: 1.1rem; line-height: 1.6;'>
                We couldn't extract the content from this article.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        ### 🤔 Common reasons:
        
        **1. Paywall or Subscription Required** 💰
        - The article requires a paid subscription
        - Content is behind a login
        - **Solution**: Try free news sources like BBC, Reuters, or AP News
        
        **2. Anti-Bot Protection** 🤖
        - Website blocks automated access
        - Cloudflare or similar protection
        - **Solution**: Try articles from mainstream news sites
        
        **3. Dynamic Content Loading** ⚡
        - Content loads via JavaScript
        - Single-page application (SPA)
        - **Solution**: Choose traditional news websites
        
        **4. Unsupported Format** 📰
        - Video-only content
        - Podcast or audio article
        - **Solution**: Select text-based articles
        
        ### ✅ Recommended Sources:
        - BBC News (https://www.bbc.com/news)
        - Reuters (https://www.reuters.com)
        - Associated Press (https://apnews.com)
        - The Guardian (https://www.theguardian.com)
        - NPR (https://www.npr.org)
        """
    )


def show_success_message(message: str, icon: str = "✅"):
    st.markdown(
        f"""
        <div style='background: linear-gradient(135deg, rgba(76, 175, 80, 0.2) 0%, rgba(56, 142, 60, 0.2) 100%);
                    padding: 1.5rem;
                    border-radius: 12px;
                    border-left: 4px solid #4caf50;
                    margin: 1rem 0;'>
            <div style='display: flex; align-items: center;'>
                <span style='font-size: 2rem; margin-right: 1rem;'>{icon}</span>
                <p style='color: #e0e0e0; margin: 0; font-size: 1.1rem; font-weight: 500;'>
                    {message}
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
