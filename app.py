import streamlit as st
import os
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Sunday Quiz", layout="wide")

# CSS для красивого оформления (оптимизирован под мобильные)
st.markdown("""
    <style>
    .stApp { 
        background-color: #f4f8fb; 
    }
    /* Заголовки и основной текст — всегда тёмные */
    h1, h2, h3, h4, h5, h6,
    .stMarkdown, .stMarkdown p, .stCaption,
    label, .stTextArea label {
        color: #1a1a1a !important;
    }
    /* Радио-кнопки */
    div[role="radiogroup"] {
        gap: 10px;
    }
    div[role="radiogroup"] > label {
        background-color: #ffffff !important;
        padding: 14px 18px;
        border-radius: 12px;
        border: 1px solid #e1e8ed;
        box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.03);
        width: 100%;
        cursor: pointer;
        transition: all 0.2s ease;
    }
    /* Принудительно тёмный текст внутри радио-кнопок */
    div[role="radiogroup"] > label p,
    div[role="radiogroup"] > label span,
    div[role="radiogroup"] > label div {
        color: #1a1a1a !important;
        font-size: 1rem;
    }
    div[role="radiogroup"] > label:hover {
        border-color: #ff4b4b;
    }
    /* Поле комментария */
    .stTextArea textarea {
        color: #1a1a1a !important;
        background-color: #ffffff !important;
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
            padding: 12px 14px;
        }
        div[role="radiogroup"] > label p,
        div[role="radiogroup"] > label span {
            font-size: 0.95rem !important;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Инициализация состояния
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'comments' not in st.session_state:
    st.session_state.comments = {}

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
        "title": "Как вам концепция квеста в лабиринте на два игрока?",
        "description": (
            "**Квест в лабиринте на два игрока, где один ищет выход, а второй выстраивает его маршрут по камерам в реальном времени... Конечно если один из них не является предателем.**\n\n"
            "Вы оказываетесь в ловушке холодного, погружённого во мрак комплекса. Игра предлагает примерить одну из двух ролей: бегуна, ищущего выход среди десятков слабо освещённых комнат, или оператора, который наблюдает за лабиринтом через сеть уцелевших видеокамер.\n\n"
            "Вашей первичной целью станет совместный побег. Оператору предстоит выстраивать безопасный маршрут в реальном времени, а бегуну — полагаться на его подсказки, чтобы миновать запутанные коридоры, скрытые во тьме тупики и смертоносные механизмы.\n\n"
            "Однако главная опасность кроется не в ловушках, а в голосе на другом конце рации. Вы никогда не можете быть до конца уверены в своём напарнике, ведь любой из вас (а иногда и оба!) может оказаться предателем. Для предателя приоритеты кардинально меняются: вместо спасения команды вам предстоит хладнокровно устранить своего спутника, заманив его в западню или навсегда заперев во тьме, а если вы вдруг узнали что предателем является ваш напарник то вам необходимо как можно быстрее в одиночку выбраться из лабиринта, оставив его там навсегда.\n\n"
            "Вам придётся шаг за шагом преодолевать страх неизвестности, анализировать каждое действие напарника и в конечном счёте решить: готовы ли вы доверить свою жизнь этому человеку чтобы сбежать вместе, или постараетесь сбежать без него и оставите здесь, возможно, навсегда?"
        ),
        "options": [
            "Очень нравится",
            "Скорее нравится, чем нет",
            "Ну спорно",
            "Скорее нет, чем да",
            "Вообще нет"
        ],
        "image": "maze.jpg"
    },
    {
        "title": "Как вам концепция экшен-рогалика с вселением в тела врагов?",
        "description": (
            "**Представьте экшен-рогалик, где у вас нет собственного оружия, а единственный способ двигаться вперед - вселиться в тело врага и управлять им... пока оно не разлетится на куски.**\n\n"
            "Вы играете за бестелесную душу в глубинах древнего подземелья. Могущественный волшебник пал от предательства соратников, лишившись тела и сил. Все что осталось, это хрупкий дух с бессмертным желанием выбраться и отомстить. Когда твоя личность грозит развеяться от любого сквозняка, морали уже нет. И некромантия уже не зло, а единственный способ существования.\n\n"
            "А еще это способ сражаться с врагами. Побеждая монстра, вы можете занять его тело, перенимая его атаки и уникальные способности — будь то тяжелый щит, дальнобойные стрелы или заклинание полета. Конечно, захваченные тела не бессмертны, однако даже получение урона может сыграть вам на руку. Когда у подчиненной тушки кончается здоровье, вы эффектно сбрасываете ее прямо в центре отряда противников, активируя уникальный посмертный эффект. Взрыв, отравляющее облако или область безумия - вариантов много, вы сможете наблюдать их со стороны, перелетев в следующее подходящее тело.\n\n"
            "Геймплей поощряет высокий темп и точный расчет. Выживание зависит от умения на ходу адаптироваться к разным боевым стилям, грамотно выстраивать цепочки целей, а главное: превращать силу врагов в свою собственную. Сможете ли вы освоить мувсет каждого монстра подземелья, собрать идеальный билд и дойти до конца, чтобы сразиться с предателями и открыть тайну собственной смерти?"
        ),
        "options": [
            "Очень нравится",
            "Скорее нравится, чем нет",
            "Ну спорно",
            "Скорее нет, чем да",
            "Вообще нет"
        ],
        "image": "soul.jpg"
    }
]

total_steps = len(questions)
current_step = st.session_state.step

# Функция сохранения результатов в CSV
def save_results(answers, comments):
    csv_file = "results.csv"
    data = {"Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    for idx, q in enumerate(questions, start=1):
        data[f"Шаг {idx} (Ответ)"] = answers.get(f"q_{idx}", "")
        data[f"Шаг {idx} (Комментарий)"] = comments.get(f"comment_{idx}", "")
    
    df_new = pd.DataFrame([data])
    if os.path.exists(csv_file):
        df_new.to_csv(csv_file, mode='a', header=False, index=False, encoding='utf-8-sig')
    else:
        df_new.to_csv(csv_file, mode='w', header=True, index=False, encoding='utf-8-sig')

# Основной интерфейс — одна колонка (мобильная версия)
if current_step <= total_steps:
    q_data = questions[current_step - 1]
    
    st.progress((current_step - 1) / total_steps)
    st.caption(f"шаг {current_step}/{total_steps}")
    st.markdown(f"## **{q_data['title']}**")
    st.caption("Выберите один ответ")
    
    # Описание игры — в раскрывающемся блоке, чтобы не занимало весь экран
    if q_data["description"]:
        with st.expander("📖 Описание игры", expanded=False):
            st.info(q_data["description"])
    
    # Радио-кнопки с ответами
    previous_choice = st.session_state.answers.get(f"q_{current_step}")
    if previous_choice in q_data["options"]:
        default_index = q_data["options"].index(previous_choice)
    else:
        default_index = None

    selected_option = st.radio(
        label="Options",
        options=q_data["options"],
        index=default_index,
        key=f"radio_{current_step}",
        label_visibility="collapsed"
    )
    
    # Комментарий
    comment = st.text_area(
        "Комментарий (необязательно):",
        value=st.session_state.comments.get(f"comment_{current_step}", ""),
        key=f"comment_input_{current_step}",
        placeholder="Здесь можно написать свой комментарий...",
        height=100
    )
    
    st.write("")
    
    # Кнопки навигации
    col_prev, col_next = st.columns([1, 1])
    with col_prev:
        if st.button("← Назад", disabled=(current_step == 1), use_container_width=True):
            st.session_state.step -= 1
            st.rerun()
    with col_next:
        if st.button("Далее →", type="primary", disabled=(selected_option is None), use_container_width=True):
            st.session_state.answers[f"q_{current_step}"] = selected_option
            st.session_state.comments[f"comment_{current_step}"] = comment
            if current_step == total_steps:
                save_results(st.session_state.answers, st.session_state.comments)
            st.session_state.step += 1
            st.rerun()
    
    st.write("")
    
    # Картинка — внизу, чтобы не мешала отвечать
    image_path = q_data["image"]
    if os.path.exists(image_path):
        st.image(image_path, use_container_width=True)
    else:
        st.image("https://cdn.pixabay.com/photo/2017/01/06/19/15/soap-1958683_1280.jpg", use_container_width=True)

else:
    st.balloons()
    st.success("Спасибо за прохождение опроса!")
    
    if st.button("Пройти заново", type="primary", use_container_width=True):
        st.session_state.step = 1
        st.session_state.answers = {}
        st.session_state.comments = {}
        st.rerun()

# --- СЕКРЕТНАЯ АДМИН-ПАНЕЛЬ ---
query_params = st.query_params
is_admin = query_params.get("admin") == "true"

if is_admin:
    with st.sidebar:
        st.title("Панель администратора")
        admin_pass = st.text_input("Пароль:", type="password")
        
        correct_password = st.secrets.get("admin", {}).get("password", "1234")
        
        if admin_pass == correct_password:
            st.success("Доступ разрешён")
            st.subheader("Сохранённые ответы:")
            if os.path.exists("results.csv"):
                df = pd.read_csv("results.csv", encoding='utf-8-sig')
                st.dataframe(df)
                st.download_button(
                    "Скачать CSV", 
                    data=df.to_csv(index=False, encoding='utf-8-sig'), 
                    file_name="results.csv", 
                    mime="text/csv"
                )
                
                st.write("---")
                st.caption("⚠️ Опасная зона")
                if st.button("🗑️ Очистить все результаты"):
                    os.remove("results.csv")
                    st.success("Все результаты удалены!")
                    st.rerun()
            else:
                st.info("Ответов пока нет.")
        elif admin_pass:
            st.error("Неверный пароль")
