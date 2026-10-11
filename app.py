st.markdown(f"""
    <style>
    /* Фон — БЕЗ fixed, так быстрее на телефоне */
    .stApp {{ 
        background-image: url("{current_bg}") !important;
        background-size: cover !important;
        background-position: center !important;
        background-repeat: no-repeat !important;
    }}
    
    .stApp::before {{
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.12);
        z-index: -1;
        pointer-events: none;
    }}
    
    /* === ЗАГОЛОВКИ И ПОДПИСИ === */
    h1, h2, h3, h4, h5, h6 {{
        color: {text_color} !important;
        font-weight: 900 !important;
        text-shadow: {heading_shadow} !important;
    }}
    .stMarkdown, .stMarkdown p {{
        color: {text_color} !important;
        font-weight: 700 !important;
    }}
    .stCaption, [data-testid="stCaptionContainer"],
    [data-testid="stCaptionContainer"] p {{
        color: {text_color} !important;
        font-weight: 700 !important;
        opacity: 1 !important;
        text-shadow: {heading_shadow} !important;
    }}
    
    /* === РАСКРЫВАЮЩИЙСЯ БЛОК === */
    div[data-testid="stExpander"] {{
        background-color: rgba(255, 255, 255, 0.95) !important;
        border: 1px solid #1a1a1a !important;
        border-radius: 8px !important;
        overflow: hidden !important;
        box-shadow: none !important;
    }}
    div[data-testid="stExpander"] summary {{
        background-color: rgba(255, 255, 255, 0.95) !important;
        padding: 14px 16px !important;
        cursor: pointer !important;
        list-style: none !important;
    }}
    div[data-testid="stExpander"] summary:hover {{
        background-color: #f5f5f5 !important;
    }}
    div[data-testid="stExpander"] summary * {{
        color: #1a1a1a !important;
        -webkit-text-fill-color: #1a1a1a !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        text-shadow: none !important;
    }}
    div[data-testid="stExpander"] .stMarkdown p,
    div[data-testid="stExpander"] [data-testid="stMarkdownContainer"] p {{
        color: #1a1a1a !important;
        -webkit-text-fill-color: #1a1a1a !important;
        font-weight: 500 !important;
        text-shadow: none !important;
    }}
    
    /* === РАДИО-КНОПКИ — без плашек === */
    div[role="radiogroup"] {{
        gap: 4px !important;
    }}
    div[role="radiogroup"] > label {{
        background: transparent !important;
        padding: 8px 4px !important;
        border: none !important;
        border-radius: 0 !important;
        box-shadow: none !important;
        width: 100% !important;
        cursor: pointer !important;
        display: flex !important;
        align-items: center !important;
    }}
    div[role="radiogroup"] > label:hover {{
        background-color: rgba(255, 75, 75, 0.08) !important;
    }}
    
    /* ⚠️ ВОЗВРАЩАЕМ ШИРОКИЕ СЕЛЕКТОРЫ для текста вариантов */
    div[role="radiogroup"] > label,
    div[role="radiogroup"] > label *,
    div[role="radiogroup"] > label p,
    div[role="radiogroup"] > label span,
    div[role="radiogroup"] > label div,
    div[role="radiogroup"] > label label,
    div[role="radiogroup"] > label [class*="st-"],
    div[role="radiogroup"] > label [data-testid],
    div[role="radiogroup"] > label [data-testid] *,
    div[role="radiogroup"] > label [data-testid="stMarkdownContainer"],
    div[role="radiogroup"] > label [data-testid="stMarkdownContainer"] p,
    div[role="radiogroup"] > label [data-baseweb] *,
    div[role="radiogroup"] > label [data-baseweb="radio"] *,
    div[role="radiogroup"] label p,
    div[role="radiogroup"] label span {{
        color: {card_text} !important;
        -webkit-text-fill-color: {card_text} !important;
        font-size: 1.15rem !important;
        font-weight: 800 !important;
        cursor: pointer !important;
        opacity: 1 !important;
        visibility: visible !important;
        text-shadow: {heading_shadow} !important;
    }}
    
    /* Кружок радио-кнопки */
    div[role="radiogroup"] > label > div:first-child > div:first-child,
    div[role="radiogroup"] label [data-baseweb="radio"] > div:first-child {{
        background-color: rgba(255, 255, 255, 0.95) !important;
        border: 2px solid #b0b8c1 !important;
        border-radius: 50% !important;
        width: 22px !important;
        height: 22px !important;
        margin-right: 10px !important;
        flex-shrink: 0 !important;
    }}
    
    /* === МЕТКА "Комментарий" === */
    .stTextArea label,
    .stTextArea label p {{
        color: {text_color} !important;
        font-weight: 800 !important;
        text-shadow: {heading_shadow} !important;
    }}
    
    /* === ПОЛЕ КОММЕНТАРИЯ === */
    .stTextArea textarea {{
        color: #1a1a1a !important;
        -webkit-text-fill-color: #1a1a1a !important;
        background-color: rgba(255, 255, 255, 0.95) !important;
        font-size: 1rem !important;
    }}
    .stTextArea textarea::placeholder {{
        color: #999999 !important;
        -webkit-text-fill-color: #999999 !important;
    }}
    
    /* === КНОПКИ НАВИГАЦИИ — быстрый отклик === */
    .stButton > button {{
        transition: background-color 0.1s ease !important;
        -webkit-tap-highlight-color: rgba(255, 75, 75, 0.2) !important;
    }}
    
    /* === МОБИЛЬНАЯ АДАПТАЦИЯ === */
    @media (max-width: 768px) {{
        .block-container {{
            padding-left: 1rem !important;
            padding-right: 1rem !important;
            padding-top: 1rem !important;
        }}
        h2 {{ 
            font-size: 1.4rem !important; 
            line-height: 1.3 !important;
        }}
    }}
    </style>
""", unsafe_allow_html=True)
