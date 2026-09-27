import streamlit as st
import os
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Sunday Quiz", layout="wide")

# CSS для красивого оформления
st.markdown("""
    <style>
    .stApp { 
        background-color: #f4f8fb; 
    }
    div[role="radiogroup"] {
        gap: 10px;
    }
    div[role="radiogroup"] > label {
        background-color: #ffffff;
        padding: 14px 20px;
        border-radius: 12px;
        border: 1px solid #e1e8ed;
        box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.03);
        width: 100%;
        cursor: pointer;
        transition: all 0.2s ease;
    }
    div[role="radiogroup"] > label:hover {
        border-color: #ff4b4b;
    }
    </style>
""", unsafe_allow_html=True)

# Инициализация состояния
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'answers' not in st.session_state:
    st.session_state.answers = {}

# Вопросы
questions = [
    {
        "title": "Как вам концепция игры про автоматизацию улья?",
        "description": (
            "**Строительство фабрики внутри улья, доведённое до абсолюта.**\n\n"
            "Вы — пчела, которой наскучила ежедневная рутина, поэтому вы решаете "
            "автоматизировать добычу и обработку по максимуму.\n\n"
            "Вашей первичной целью станет постройка небольшого завода по производству мёда "
            "и его транспортировка, причём чем выше эффективность вашего завода, тем больше "
            "последователей (работников) примкнёт к вашему «инженерному улью».\n\n"
            "Вы столкнётесь со сложностями в виде Королевы улья. Ей не нравится, что пчёлы "
            "выходят из её подчинения, выбирая продвинутые методы развития. По мере роста "
            "популяции вы столкнётесь с репрессиями, санкциями и законами, усложняющими "
            "постройку новых механизмов или запрещающими работу на старых.\n\n"
            "Придётся выстраивать логистические цепочки с учётом «завтра», принимать "
            "антикризисные решения и в конечном счёте добиться подавляющего большинства "
            "сторонников в улье!"
        ),
        "options": [
            "Очень нравится",
            "Скорее нравится, чем нет",
            "Ну спорно",
            "Скорее нет, чем да",
            "Вообще нет"
        ],
        "image": "bees.jpg"
    },
    {
        "title": "Какова ваша цель?",
        "description": "",
        "options": [
            "Расслабиться и отдохнуть",
            "Развивать воображение и творческие способности",
            "Исследовать новые идеи и концепции",
            "Расширять знания и понимание"
        ],
        "image": "bees.jpg"
    },
    {
        "title": "Сколько у вас есть времени?",
        "description": "",
        "options": ["5-10 минут", "15-30 минут", "1+ час"],
        "image": "bees.jpg"
    },
    {
        "title": "Выберите предпочитаемый формат:",
        "description": "",
        "options": ["Текст", "Аудио", "Интерактив"],
        "image": "bees.jpg"
    }
]

total_steps = len(questions)
current_step = st.session_state.step

# Функция сохранения результатов в CSV
def save_results(answers):
    csv_file = "results.csv"
    data = {"Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    for idx, q in enumerate(questions, start=1):
        data[f"Шаг {idx}: {q['title']}"] = answers.get(f"q_{idx}", "")
    
    df_new = pd.DataFrame([data])
    if os.path.exists(csv_file):
        df_new.to_csv(csv_file, mode='a', header=False, index=False, encoding='utf-8-sig')
    else:
        df_new.to_csv(csv_file, mode='w', header=True, index=False, encoding='utf-8-sig')

# Основной интерфейс
if current_step <= total_steps:
    q_data = questions[current_step - 1]
    
    col_left, col_right = st.columns([1, 1.2], gap="large")
    
    with col_left:
        st.caption(f"шаг {current_step}/{total_steps}")
        st.markdown(f"## **{q_data['title']}**")
        st.caption("Выберите один ответ")

        previous_choice = st.session_state.answers.get(f"q_{current_step}", q_data["options"][0])
        default_index = q_data["options"].index(previous_choice) if previous_choice in q_data["options"] else 0

        selected_option = st.radio(
            label="Options",
            options=q_data["options"],
            index=default_index,
            key=f"radio_{current_step}",
            label_visibility="collapsed"
        )

        st.write("")
        col_prev, col_next, _ = st.columns([1, 1, 2])
        
        with col_prev:
            if st.button("←", disabled=(current_step == 1)):
                st.session_state.step -= 1
                st.rerun()

        with col_next:
            if st.button("→", type="primary"):
                st.session_state.answers[f"q_{current_step}"] = selected_option
                if current_step == total_steps:
                    save_results(st.session_state.answers)
                st.session_state.step += 1
                st.rerun()

    with col_right:
        if q_data["description"]:
            st.info(q_data["description"])
            
        image_path = q_data["image"]
        if os.path.exists(image_path):
            st.image(image_path, use_container_width=True)
        else:
            st.image("https://cdn.pixabay.com/photo/2017/01/06/19/15/soap-1958683_1280.jpg", use_container_width=True)

else:
    st.balloons()
    st.success("Спасибо за прохождение опроса!")
    
    if st.button("Пройти заново", type="primary"):
        st.session_state.step = 1
        st.session_state.answers = {}
        st.rerun()

# Скрытая панель администратора для просмотра результатов
with st.sidebar:
    st.title("Панель администратора")
    admin_pass = st.text_input("Пароль:", type="password")
    if admin_pass == "1234":  # Ваш пароль для просмотра результатов
        st.subheader("Сохранённые ответы:")
        if os.path.exists("results.csv"):
            df = pd.read_csv("results.csv", encoding='utf-8-sig')
            st.dataframe(df)
            st.download_button("Скачать CSV", data=df.to_csv(index=False, encoding='utf-8-sig'), file_name="results.csv", mime="text/csv")
        else:
            st.info("Ответов пока нет.")