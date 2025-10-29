import streamlit as st


def apply_custom_styles():
    """
    Apply modern, professional CSS styling to the Streamlit app.
    Dark theme with proper contrast and visibility.
    """
    st.markdown(
        """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@500;700&display=swap');
        
        * {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        }
        
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
            background: linear-gradient(135deg, #0a0e27 0%, #1a1a2e 50%, #16213e 100%) !important;
        }
        
        .main, [data-testid="stMain"] {
            background: transparent !important;
            padding: 2rem 1rem;
        }
        
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 1200px;
            background: transparent !important;
        }
        
        section[data-testid="stSidebar"],
        section[data-testid="stMainMenu"],
        .stApp > header,
        [data-testid="stHeader"] {
            background: #0f3460 !important;
        }
        
        [data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] {
            background: transparent !important;
        }
        
        .stMarkdown, p, span, div, label {
            color: #e0e0e0 !important;
        }
        
        .main-header {
            font-family: 'Space Grotesk', sans-serif;
            font-size: clamp(2.5rem, 5vw, 4rem);
            font-weight: 700;
            text-align: center;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: white;
            background-clip: text;
            margin-bottom: 0.5rem;
            letter-spacing: -0.02em;
            animation: fadeInUp 0.6s ease-out;
        }
        
        .sub-header {
            font-size: clamp(1rem, 2vw, 1.25rem);
            text-align: center;
            color: #b0b0b0 !important;
            margin-bottom: 3rem;
            font-weight: 400;
            animation: fadeInUp 0.8s ease-out;
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateX(-20px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }
        
        @keyframes pulse {
            0%, 100% {
                transform: scale(1);
            }
            50% {
                transform: scale(1.05);
            }
        }
        
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0f3460 0%, #16213e 100%) !important;
            border-right: 1px solid #533483;
        }
        
        [data-testid="stSidebar"] > div:first-child {
            background: transparent !important;
        }
        
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h2,
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h3 {
            color: #ffffff !important;
            font-weight: 600;
            font-size: 1.1rem;
            margin-top: 1rem;
        }
        
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] div {
            color: #e0e0e0 !important;
        }
        
        [data-testid="stSidebar"] .stRadio > label {
            font-weight: 500;
            color: #ffffff !important;
        }
        
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] strong {
            color: #ffffff !important;
        }
        
        .score-container {
            padding: 2.5rem;
            border-radius: 20px;
            text-align: center;
            margin: 1.5rem 0;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
            border: 1px solid rgba(255, 255, 255, 0.1);
            position: relative;
            overflow: hidden;
            animation: fadeInUp 0.6s ease-out;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .score-container:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.6);
        }
        
        .score-container::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, 
                rgba(255,255,255,0.3) 0%, 
                rgba(255,255,255,0.8) 50%, 
                rgba(255,255,255,0.3) 100%);
        }
        
        .high-credibility {
            background: linear-gradient(135deg, 
                rgba(76, 175, 80, 0.95) 0%, 
                rgba(56, 142, 60, 0.95) 100%);
            color: white;
        }
        
        .medium-credibility {
            background: linear-gradient(135deg, 
                rgba(255, 152, 0, 0.95) 0%, 
                rgba(245, 124, 0, 0.95) 100%);
            color: white;
        }
        
        .low-credibility {
            background: linear-gradient(135deg, 
                rgba(244, 67, 54, 0.95) 0%, 
                rgba(229, 57, 53, 0.95) 100%);
            color: white;
        }
        
        .score-container h1 {
            font-size: 3rem;
            font-weight: 700;
            margin: 0.5rem 0;
            color: #ffffff !important;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
            animation: pulse 2s ease-in-out infinite;
        }
        
        .score-container h3 {
            font-size: 1.1rem;
            font-weight: 500;
            margin: 0;
            color: #ffffff !important;
            opacity: 0.95;
        }
        
        .score-container div {
            color: #ffffff !important;
        }
        
        .article-card {
            padding: 2rem;
            border: 1px solid #533483;
            border-radius: 16px;
            margin: 1.5rem 0;
            background: linear-gradient(135deg, rgba(15, 52, 96, 0.95) 0%, rgba(22, 33, 62, 0.95) 100%);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
            position: relative;
            overflow: hidden;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            animation: slideIn 0.5s ease-out;
            backdrop-filter: blur(10px);
        }
        
        .article-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 4px;
            height: 100%;
            background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
        }
        
        .article-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 30px rgba(102, 126, 234, 0.4);
            border-color: #667eea;
        }
        
        .article-card h4 {
            color: #ffffff !important;
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 1rem;
            line-height: 1.4;
        }
        
        .article-card p {
            color: #b0b0b0 !important;
            line-height: 1.7;
            margin: 0.5rem 0;
        }
        
        .article-card strong {
            color: #e0e0e0 !important;
            font-weight: 600;
        }
        
        .article-card a {
            color: #667eea !important;
            text-decoration: none;
            font-weight: 500;
            display: inline-flex;
            align-items: center;
            margin-top: 1rem;
            transition: all 0.2s ease;
        }
        
        .article-card a:hover {
            color: #764ba2 !important;
            transform: translateX(5px);
        }
        
        .article-card div {
            color: #e0e0e0 !important;
        }
        
        .article-card span {
            color: #b0b0b0 !important;
        }
        
        .claim-box {
            padding: 1.5rem;
            border-left: 4px solid #667eea;
            background: linear-gradient(135deg, rgba(15, 52, 96, 0.95) 0%, rgba(22, 33, 62, 0.95) 100%);
            margin: 1rem 0;
            border-radius: 12px;
            color: #e0e0e0 !important;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.4);
            transition: all 0.3s ease;
            animation: slideIn 0.4s ease-out;
            backdrop-filter: blur(10px);
        }
        
        .claim-box:hover {
            transform: translateX(8px);
            box-shadow: 0 4px 16px rgba(102, 126, 234, 0.4);
        }
        
        .claim-box strong {
            color: #ffffff !important;
            font-size: 1.05rem;
        }
        
        .claim-box small {
            color: #b0b0b0 !important;
            font-style: italic;
        }
        
        .claim-box div {
            color: #e0e0e0 !important;
        }
        
        .badge {
            display: inline-block;
            padding: 0.4rem 1rem;
            border-radius: 50px;
            font-size: 0.875rem;
            font-weight: 600;
            margin: 0.5rem 0.25rem;
            transition: all 0.2s ease;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .badge:hover {
            transform: scale(1.05);
        }
        
        .badge-success {
            background: linear-gradient(135deg, #4caf50 0%, #66bb6a 100%);
            color: white !important;
            box-shadow: 0 4px 12px rgba(76, 175, 80, 0.4);
        }
        
        .badge-warning {
            background: linear-gradient(135deg, #ff9800 0%, #ffa726 100%);
            color: white !important;
            box-shadow: 0 4px 12px rgba(255, 152, 0, 0.4);
        }
        
        .badge-danger {
            background: linear-gradient(135deg, #f44336 0%, #ef5350 100%);
            color: white !important;
            box-shadow: 0 4px 12px rgba(244, 67, 54, 0.4);
        }
        
        .badge-info {
            background: linear-gradient(135deg, #2196f3 0%, #42a5f5 100%);
            color: white !important;
            box-shadow: 0 4px 12px rgba(33, 150, 243, 0.4);
        }
        
        .stButton > button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
            color: white !important;
            border: none !important;
            border-radius: 12px !important;
            padding: 0.75rem 2rem !important;
            font-weight: 600 !important;
            font-size: 1rem !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4) !important;
            cursor: pointer;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6) !important;
            background: linear-gradient(135deg, #764ba2 0%, #667eea 100%) !important;
        }
        
        .stButton > button:active {
            transform: translateY(0) !important;
        }
        
        .stTextInput > div > div > input {
            border-radius: 12px !important;
            border: 2px solid #533483 !important;
            padding: 0.75rem 1rem !important;
            font-size: 1rem !important;
            transition: all 0.3s ease !important;
            background: rgba(15, 52, 96, 0.6) !important;
            color: #ffffff !important;
        }
        
        .stTextInput > div > div > input::placeholder {
            color: #8892b0 !important;
        }
        
        .stTextInput > div > div > input:focus {
            border-color: #667eea !important;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.3) !important;
            outline: none !important;
            background: rgba(15, 52, 96, 0.9) !important;
        }
        
        .stTextInput > label {
            color: #e0e0e0 !important;
            font-weight: 500 !important;
        }
        
        .streamlit-expanderHeader {
            background: rgba(15, 52, 96, 0.8) !important;
            border-radius: 12px !important;
            border: 1px solid #533483 !important;
            padding: 1rem 1.5rem !important;
            font-weight: 500 !important;
            color: #ffffff !important;
            transition: all 0.3s ease !important;
            backdrop-filter: blur(10px);
        }
        
        .streamlit-expanderHeader:hover {
            background: rgba(22, 33, 62, 0.9) !important;
            border-color: #667eea !important;
        }
        
        .streamlit-expanderContent {
            background: rgba(15, 52, 96, 0.6) !important;
            border: 1px solid #533483 !important;
            border-top: none !important;
            border-radius: 0 0 12px 12px !important;
            color: #e0e0e0 !important;
            backdrop-filter: blur(10px);
        }
        
        [data-testid="stMetricValue"] {
            font-size: 2rem !important;
            font-weight: 700 !important;
            color: #ffffff !important;
        }
        
        [data-testid="stMetricLabel"] {
            font-size: 0.9rem !important;
            font-weight: 500 !important;
            color: #b0b0b0 !important;
            text-transform: uppercase !important;
            letter-spacing: 0.5px !important;
        }
        
        [data-testid="stMetricDelta"] {
            font-size: 0.9rem !important;
            font-weight: 600 !important;
        }
        
        .stSpinner > div {
            border-color: #667eea transparent transparent transparent !important;
        }
        
        .stAlert {
            border-radius: 12px !important;
            border: none !important;
            padding: 1rem 1.5rem !important;
            animation: slideIn 0.4s ease-out !important;
            backdrop-filter: blur(10px);
        }
        
        [data-baseweb="notification"] {
            border-radius: 12px !important;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5) !important;
            background: rgba(15, 52, 96, 0.9) !important;
            color: #e0e0e0 !important;
            backdrop-filter: blur(10px);
        }
        
        div[data-baseweb="notification"][kind="info"] {
            background: rgba(33, 150, 243, 0.3) !important;
            border-left: 4px solid #2196f3 !important;
            color: #ffffff !important;
        }
        
        div[data-baseweb="notification"][kind="warning"] {
            background: rgba(255, 152, 0, 0.3) !important;
            border-left: 4px solid #ff9800 !important;
            color: #ffffff !important;
        }
        
        div[data-baseweb="notification"][kind="error"] {
            background: rgba(244, 67, 54, 0.3) !important;
            border-left: 4px solid #f44336 !important;
            color: #ffffff !important;
        }
        
        div[data-baseweb="notification"][kind="success"] {
            background: rgba(76, 175, 80, 0.3) !important;
            border-left: 4px solid #4caf50 !important;
            color: #ffffff !important;
        }
        
        .js-plotly-plot {
            border-radius: 12px !important;
            overflow: hidden !important;
            background: rgba(15, 52, 96, 0.8) !important;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5) !important;
            backdrop-filter: blur(10px);
        }
        
        h2, h3 {
            color: #ffffff !important;
            font-weight: 600 !important;
            margin-top: 2rem !important;
            margin-bottom: 1rem !important;
            position: relative !important;
            padding-left: 1rem !important;
        }
        
        h2::before {
            content: '';
            position: absolute;
            left: 0;
            top: 50%;
            transform: translateY(-50%);
            width: 4px;
            height: 60%;
            background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
            border-radius: 2px;
        }
        
        code {
            background: rgba(15, 52, 96, 0.8) !important;
            color: #667eea !important;
            padding: 0.2rem 0.5rem !important;
            border-radius: 4px !important;
            border: 1px solid #533483 !important;
        }
        
        pre {
            background: rgba(15, 52, 96, 0.8) !important;
            border: 1px solid #533483 !important;
            border-radius: 8px !important;
            padding: 1rem !important;
        }
        
        @media (max-width: 768px) {
            .main-header {
                font-size: 2rem !important;
            }
            
            .sub-header {
                font-size: 1rem !important;
            }
            
            .score-container {
                padding: 1.5rem !important;
            }
            
            .score-container h1 {
                font-size: 2rem !important;
            }
            
            .article-card {
                padding: 1.5rem !important;
            }
            
            .block-container {
                padding-top: 1rem !important;
                padding-bottom: 1rem !important;
            }
        }
        
        ::-webkit-scrollbar {
            width: 10px;
            height: 10px;
        }
        
        ::-webkit-scrollbar-track {
            background: #16213e;
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(180deg, #764ba2 0%, #667eea 100%);
        }
        
        [data-testid="stRadio"] > label {
            color: #ffffff !important;
        }
        
        [data-testid="stRadio"] [role="radiogroup"] label {
            color: #e0e0e0 !important;
        }
        
        [data-testid="stRadio"] [role="radiogroup"] label div {
            color: #e0e0e0 !important;
        }
        
        .stMarkdown p, .stMarkdown span, .stMarkdown div, .stMarkdown li {
            color: #e0e0e0 !important;
        }
        
        [data-testid="stMarkdownContainer"] p {
            color: #e0e0e0 !important;
        }
        
        [data-testid="stMarkdownContainer"] strong {
            color: #ffffff !important;
        }
        
        [data-testid="stMarkdownContainer"] div {
            color: #e0e0e0 !important;
        }
        
        [data-testid="stMarkdownContainer"] > div {
            background: transparent !important;
        }
        
        div[data-testid="column"] {
            background: transparent !important;
        }
        
        .stProgress > div > div > div {
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%) !important;
        }
        
        [data-testid="column"] > div {
            background: transparent !important;
        }
    </style>
    """,
        unsafe_allow_html=True,
    )
