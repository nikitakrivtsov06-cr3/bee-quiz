st.markdown("""
    <style>
    .stApp { 
        background-color: #f4f8fb; 
    }
    
    /* === ЗАГОЛОВКИ И ОБЩИЙ ТЕКСТ === */
    h1, h2, h3, h4, h5, h6,
    .stMarkdown, .stMarkdown p, .stCaption,
    .stTextArea label {
        color: #1a1a1a !important;
    }
    
    /* === ЯРКИЙ РАСКРЫВАЮЩИЙСЯ БЛОК "ОПИСАНИЕ ИГРЫ" === */
    div[data-testid="stExpander"] {
        background-color: #e8f4ff !important;
        border: 2px solid #4a90e2 !important;
        border-radius: 12px !important;
        overflow: hidden !important;
        box-shadow: 0px 3px 10px rgba(74, 144, 226, 0.15) !important;
    }
    div[data-testid="stExpander"] summary {
        background-color: #e8f4ff !important;
        padding: 16px !important;
        cursor: pointer !important;
        list-style: none !important;
    }
    div[data-testid="stExpander"] summary:hover {
        background-color: #d4e9ff !important;
    }
    div[data-testid="stExpander"] summary p,
    div[data-testid="stExpander"] summary span,
    div[data-testid="stExpander"] summary div {
        color: #1a5fb4 !important;
        -webkit-text-fill-color: #1a5fb4 !important;
        font-weight: 700 !important;
        font-size: 1.05rem !important;
    }
    div[data-testid="stExpander"] summary svg {
        fill: #1a5fb4 !important;
        color: #1a5fb4 !important;
    }
    
    /* === РАДИО-КНОПКИ === */
    div[role="radiogroup"] {
        gap: 10px !important;
    }
    
    /* Плашка ответа */
    div[role="radiogroup"] > label {
        background-color: #ffffff !important;
        padding: 14px 18px !important;
        border-radius: 12px !important;
        border: 1px solid #e1e8ed !important;
        box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.03) !important;
        width: 100% !important;
        cursor: pointer !important;
        transition: all 0.2s ease !important;
        -webkit-tap-highlight-color: rgba(255, 75, 75, 0.1) !important;
        display: flex !important;
        align-items: center !important;
    }
    div[role="radiogroup"] > label:hover {
        border-color: #ff4b4b !important;
        background-color: #fff8f8 !important;
    }
    
    /* ВЕСЬ ТЕКСТ ВНУТРИ ПЛАШКИ — ТЁМНЫЙ И КЛИКАБЕЛЬНЫЙ */
    div[role="radiogroup"] > label,
    div[role="radiogroup"] > label *,
    div[role="radiogroup"] > label p,
    div[role="radiogroup"] > label span,
    div[role="radiogroup"] > label div {
        color: #1a1a1a !important;
        -webkit-text-fill-color: #1a1a1a !important;
        font-size: 1rem !important;
        cursor: pointer !important;
        user-select: none !important;
    }
    
    /* Круг радио-кнопки — белый с серой обводкой */
    /* Внутренний круг Streamlit (тот, что закрашивается) */
    div[role="radiogroup"] > label div[data-baseweb="radio"] > div:first-child,
    div[role="radiogroup"] > label > div:first-child > div:first-child {
        background-color: #ffffff !important;
        border: 2px solid #b0b8c1 !important;
        border-radius: 50% !important;
        width: 20px !important;
        height: 20px !important;
    }
    
    /* Когда выбран — красная обводка */
    div[role="radiogroup"] > label input[type="radio"]:checked + div,
    div[role="radiogroup"] > label input[type="radio"]:checked ~ div {
        border-color: #ff4b4b !important;
    }
    
    /* Поле комментария */
    .stTextArea textarea {
        color: #1a1a1a !important;
        -webkit-text-fill-color: #1a1a1a !important;
        background-color: #ffffff !important;
        font-size: 1rem !important;
    }
    .stTextArea textarea::placeholder {
        color: #999999 !important;
        -webkit-text-fill-color: #999999 !important;
    }
    
    /* Мобильная адаптация */
    @media (max-width: 768px) {
        .block-container {
            padding-left: 1rem !important;
            padding-right: 1rem !important;
            padding-top: 1rem !important;
        }
        h2 { 
            font-size: 1.35rem !important; 
            line-height: 1.3 !important;
        }
        div[role="radiogroup"] > label {
            padding: 14px 14px !important;
        }
        div[role="radiogroup"] > label,
        div[role="radiogroup"] > label *,
        div[role="radiogroup"] > label p {
            font-size: 0.98rem !important;
        }
        div[data-testid="stExpander"] summary {
            padding: 14px !important;
        }
    }
    </style>
""", unsafe_allow_html=True)
