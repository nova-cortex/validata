import streamlit as st
from typing import Dict, List, Optional
from charts import create_credibility_gauge, create_bias_chart


def display_article_verification(data: Dict):
    st.markdown("---")
    st.markdown("## 📊 Verification Results")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("### 📰 Article Information")
        article = data.get("article", {})
        st.markdown(f"**Title:** {article.get('title', 'N/A')}")
        st.markdown(f"**Author:** {article.get('author', 'Unknown')}")
        st.markdown(f"**Published:** {article.get('publish_date', 'Unknown')}")

        with st.expander("📄 Article Summary"):
            st.write(article.get("summary", "No summary available"))

    with col2:
        credibility = data.get("credibility", {})
        score = credibility.get("overall_score", 50)

        if score >= 70:
            css_class = "high-credibility"
            icon = "✅"
        elif score >= 50:
            css_class = "medium-credibility"
            icon = "⚠️"
        else:
            css_class = "low-credibility"
            icon = "❌"

        st.markdown(
            f"""
        <div class="score-container {css_class}">
            <h1>{icon} {score}/100</h1>
            <h3>{credibility.get('domain_reputation', 'Unknown Source')}</h3>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.plotly_chart(create_credibility_gauge(score), use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### ✅ Strengths")
        strengths = credibility.get("strengths", [])
        if strengths:
            for strength in strengths:
                st.markdown(f"- {strength}")
        else:
            st.info("No specific strengths identified")

    with col2:
        st.markdown("### ⚠️ Concerns")
        concerns = credibility.get("concerns", [])
        if concerns:
            for concern in concerns:
                st.markdown(f"- {concern}")
        else:
            st.success("No major concerns identified")

    col1, col2 = st.columns(2)
    with col1:
        bias = credibility.get("bias", "unknown")
        st.markdown(f"**Political Bias:** `{bias.upper()}`")
    with col2:
        sensationalism = credibility.get("sensationalism", "unknown")
        st.markdown(f"**Sensationalism Level:** `{sensationalism.upper()}`")

    st.markdown("### 🔍 Claim Verification")
    fact_checks = data.get("fact_checks", {})
    claims = fact_checks.get("claims", [])

    if claims:
        for i, claim in enumerate(claims, 1):
            verifiability = claim.get("verifiability", "Unknown")

            if verifiability == "Verifiable":
                badge = "badge-success"
            elif verifiability == "Partially Verifiable":
                badge = "badge-warning"
            else:
                badge = "badge-danger"

            st.markdown(
                f"""
            <div class="claim-box">
                <strong>Claim {i}:</strong> {claim.get('claim', 'N/A')}
                <br><span class="badge {badge}">{verifiability}</span>
                <br><small><em>{claim.get('reasoning', '')}</em></small>
            </div>
            """,
                unsafe_allow_html=True,
            )
    else:
        st.info("No specific claims analyzed")

    if fact_checks.get("manipulation_tactics"):
        st.markdown("### 🎭 Detected Manipulation Tactics")
        for tactic in fact_checks.get("manipulation_tactics", []):
            st.warning(f"⚠️ {tactic}")

    st.markdown("### 🔗 Similar Articles from Other Sources")
    similar = data.get("similar_articles", [])

    if similar:
        for article in similar[:5]:
            st.markdown(
                f"""
            <div class="article-card">
                <h4>{article.get('title', 'No title')}</h4>
                <p><strong>Source:</strong> {article.get('source', 'Unknown')}</p>
                <p>{article.get('description', 'No description')[:200]}...</p>
                <a href="{article.get('url', '#')}" target="_blank">Read Article →</a>
            </div>
            """,
                unsafe_allow_html=True,
            )
    else:
        st.info("No similar articles found")

    st.markdown("### 💡 Media Literacy Tip")
    st.info(
        """
    **Cross-Reference Multiple Sources:** Always verify important claims by checking multiple 
    reputable news sources. Different outlets may emphasize different aspects of the same story.
    """
    )


def display_news_search_results(data: Dict):
    try:
        st.markdown("---")
        st.markdown("## 🔍 News Analysis Results")

        st.markdown("### 📋 Consensus Summary")
        summary = data.get("summary", {})

        st.markdown(
            f"""
        <div class="article-card">
            <h4>Neutral Analysis</h4>
            <p>{summary.get('consensus_summary', 'No summary available')}</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### ✅ Points of Agreement")
            agreements = summary.get("points_of_agreement", [])
            if agreements:
                for point in agreements:
                    st.success(f"✓ {point}")
            else:
                st.info("No common points identified")

        with col2:
            st.markdown("#### ⚖️ Different Perspectives")
            disagreements = summary.get("points_of_disagreement", [])
            if disagreements:
                for point in disagreements:
                    st.warning(f"→ {point}")
            else:
                st.info("No major disagreements found")

        st.markdown("### 📊 Source Analysis")

        bias_analysis = data.get("bias_analysis", {})

        try:
            total_articles = bias_analysis.get("total_articles", 0)
            unique_sources = bias_analysis.get("unique_sources", 0)
            diversity_score = bias_analysis.get("diversity_score", 0)

            if isinstance(total_articles, str):
                total_articles = int(total_articles) if total_articles.isdigit() else 0
            else:
                total_articles = (
                    int(total_articles) if total_articles is not None else 0
                )

            if isinstance(unique_sources, str):
                unique_sources = int(unique_sources) if unique_sources.isdigit() else 0
            else:
                unique_sources = (
                    int(unique_sources) if unique_sources is not None else 0
                )

            if isinstance(diversity_score, str):
                diversity_score = (
                    float(diversity_score)
                    if diversity_score.replace(".", "").replace("-", "").isdigit()
                    else 0.0
                )
            else:
                diversity_score = (
                    float(diversity_score) if diversity_score is not None else 0.0
                )

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Total Articles", total_articles)
            with col2:
                st.metric("Unique Sources", unique_sources)
            with col3:
                st.metric("Source Diversity", f"{diversity_score:.1f}%")
        except Exception as metric_error:
            st.warning(f"Could not display source metrics: {str(metric_error)}")

        articles = data.get("articles", [])
        if articles and len(articles) > 0:
            try:
                fig = create_bias_chart(articles)
                if fig:
                    st.plotly_chart(fig, use_container_width=True)
            except Exception as chart_error:
                st.warning(
                    f"Could not display source distribution chart: {str(chart_error)}"
                )

        st.markdown("### 📰 All Articles")

        for i, article in enumerate(articles, 1):
            with st.expander(
                f"{i}. {article.get('title', 'No title')} - {article.get('source', 'Unknown')}"
            ):
                col1, col2 = st.columns([3, 1])

                with col1:
                    st.markdown(f"**Author:** {article.get('author', 'Unknown')}")
                    st.markdown(
                        f"**Published:** {article.get('publishedAt', 'Unknown')}"
                    )
                    st.write(article.get("description", "No description available"))
                    st.markdown(f"[Read Full Article]({article.get('url', '#')})")

                with col2:
                    if article.get("urlToImage"):
                        try:
                            st.image(
                                article.get("urlToImage"), use_container_width=True
                            )
                        except:
                            pass

        st.markdown("### 💡 Media Literacy Tip")
        tip = summary.get(
            "media_literacy_tip",
            "Notice how different outlets emphasize different aspects of the same story",
        )
        st.info(f"📚 {tip}")

    except Exception as e:
        st.error(f"Error displaying results: {str(e)}")
        import traceback

        st.code(traceback.format_exc())
