import plotly.graph_objects as go
import plotly.express as px
from typing import Dict, List, Optional


def create_credibility_gauge(score: int) -> go.Figure:
    if score >= 70:
        bar_color = "#4caf50"
    elif score >= 50:
        bar_color = "#ff9800"
    else:
        bar_color = "#f44336"

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number+delta",
            value=score,
            domain={"x": [0, 1], "y": [0, 1]},
            title={
                "text": "<b>Credibility Score</b>",
                "font": {"size": 24, "color": "#212529", "family": "Inter"},
            },
            number={
                "font": {"size": 48, "color": "#212529", "family": "Inter"},
                "suffix": "/100",
            },
            delta={
                "reference": 50,
                "increasing": {"color": "#4caf50"},
                "decreasing": {"color": "#f44336"},
            },
            gauge={
                "axis": {
                    "range": [None, 100],
                    "tickwidth": 2,
                    "tickcolor": "#e9ecef",
                    "tickfont": {"size": 14, "color": "#6c757d"},
                },
                "bar": {"color": bar_color, "thickness": 0.75},
                "bgcolor": "#f8f9fa",
                "borderwidth": 3,
                "bordercolor": "#e9ecef",
                "steps": [
                    {"range": [0, 40], "color": "rgba(244, 67, 54, 0.15)"},
                    {"range": [40, 60], "color": "rgba(255, 152, 0, 0.15)"},
                    {"range": [60, 80], "color": "rgba(76, 175, 80, 0.15)"},
                    {"range": [80, 100], "color": "rgba(76, 175, 80, 0.25)"},
                ],
                "threshold": {
                    "line": {"color": "#212529", "width": 4},
                    "thickness": 0.75,
                    "value": 70,
                },
            },
        )
    )

    fig.update_layout(
        height=350,
        margin=dict(l=40, r=40, t=80, b=40),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={"color": "#212529", "family": "Inter"},
    )

    return fig


def create_bias_chart(articles: List[Dict]) -> Optional[go.Figure]:
    if not articles:
        return None

    sources = [article.get("source", "Unknown") for article in articles]
    source_counts = {}
    for source in sources:
        source_counts[source] = source_counts.get(source, 0) + 1

    sorted_sources = sorted(source_counts.items(), key=lambda x: x[1], reverse=True)
    source_names = [s[0] for s in sorted_sources]
    count_values = [s[1] for s in sorted_sources]

    colors = []
    max_count = max(count_values) if count_values else 1
    for count in count_values:
        intensity = count / max_count
        r = int(102 + (118 - 102) * intensity)
        g = int(126 + (75 - 126) * intensity)
        b = int(234 + (162 - 234) * intensity)
        colors.append(f"rgb({r}, {g}, {b})")

    fig = go.Figure(
        data=[
            go.Bar(
                x=source_names,
                y=count_values,
                marker=dict(
                    color=colors,
                    line=dict(color="rgba(255, 255, 255, 0.5)", width=2),
                ),
                text=count_values,
                textposition="outside",
                textfont=dict(size=14, color="#212529", family="Inter"),
                hovertemplate="<b>%{x}</b><br>"
                + "Articles: %{y}<br>"
                + "<extra></extra>",
            )
        ]
    )

    fig.update_layout(
        title={
            "text": "<b>Source Distribution</b>",
            "font": {"size": 20, "color": "#212529", "family": "Inter"},
            "x": 0.5,
            "xanchor": "center",
        },
        xaxis_title="<b>News Source</b>",
        yaxis_title="<b>Number of Articles</b>",
        showlegend=False,
        height=450,
        margin=dict(l=60, r=40, t=80, b=120),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={"color": "#495057", "family": "Inter"},
        xaxis=dict(
            tickangle=-45,
            tickfont=dict(size=12, color="#6c757d"),
            gridcolor="#e9ecef",
            showgrid=False,
        ),
        yaxis=dict(
            tickfont=dict(size=12, color="#6c757d"),
            gridcolor="#e9ecef",
            showgrid=True,
            gridwidth=1,
        ),
        hoverlabel=dict(
            bgcolor="white",
            font_size=14,
            font_family="Inter",
            bordercolor="#667eea",
        ),
    )

    return fig


def create_detailed_scores_chart(scores: Dict) -> go.Figure:
    categories = [
        "Source Reputation",
        "Writing Quality",
        "Evidence Quality",
        "Objectivity",
        "Transparency",
    ]

    values = [
        scores.get("source_reputation", 5),
        scores.get("writing_quality", 5),
        scores.get("evidence_quality", 5),
        scores.get("objectivity", 5),
        scores.get("transparency", 5),
    ]

    values_closed = values + [values[0]]
    categories_closed = categories + [categories[0]]

    fig = go.Figure()

    fig.add_trace(
        go.Scatterpolar(
            r=values_closed,
            theta=categories_closed,
            fill="toself",
            fillcolor="rgba(102, 126, 234, 0.3)",
            line=dict(color="rgb(102, 126, 234)", width=3),
            marker=dict(size=8, color="rgb(102, 126, 234)"),
            name="Scores",
            hovertemplate="<b>%{theta}</b><br>"
            + "Score: %{r}/10<br>"
            + "<extra></extra>",
        )
    )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10],
                tickfont=dict(size=12, color="#6c757d"),
                gridcolor="#e9ecef",
            ),
            angularaxis=dict(
                tickfont=dict(size=13, color="#495057", family="Inter"),
            ),
        ),
        showlegend=False,
        height=400,
        margin=dict(l=80, r=80, t=80, b=80),
        paper_bgcolor="rgba(0,0,0,0)",
        font={"family": "Inter"},
        hoverlabel=dict(
            bgcolor="white",
            font_size=14,
            font_family="Inter",
            bordercolor="#667eea",
        ),
    )

    return fig


def create_timeline_chart(articles: List[Dict]) -> Optional[go.Figure]:
    if not articles:
        return None

    dates = []
    sources = []
    titles = []

    for article in articles:
        pub_date = article.get("publishedAt", "")
        if pub_date:
            dates.append(pub_date[:10])
            sources.append(article.get("source", "Unknown"))
            titles.append(article.get("title", "No title")[:50] + "...")

    if not dates:
        return None

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=dates,
            y=sources,
            mode="markers+text",
            marker=dict(
                size=12,
                color="#667eea",
                line=dict(color="white", width=2),
            ),
            text=["📰"] * len(dates),
            textposition="middle center",
            hovertemplate="<b>%{y}</b><br>" + "Date: %{x}<br>" + "<extra></extra>",
        )
    )

    fig.update_layout(
        title={
            "text": "<b>Publication Timeline</b>",
            "font": {"size": 20, "color": "#212529", "family": "Inter"},
            "x": 0.5,
            "xanchor": "center",
        },
        xaxis_title="<b>Publication Date</b>",
        yaxis_title="<b>News Source</b>",
        height=400,
        margin=dict(l=150, r=40, t=80, b=80),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={"color": "#495057", "family": "Inter"},
        xaxis=dict(
            tickfont=dict(size=12, color="#6c757d"),
            gridcolor="#e9ecef",
            showgrid=True,
        ),
        yaxis=dict(
            tickfont=dict(size=11, color="#6c757d"),
            gridcolor="#e9ecef",
            showgrid=True,
        ),
        hoverlabel=dict(
            bgcolor="white",
            font_size=14,
            font_family="Inter",
            bordercolor="#667eea",
        ),
    )

    return fig
