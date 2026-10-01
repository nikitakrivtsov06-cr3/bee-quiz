import streamlit as st
import os
import pandas as pd
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials

st.set_page_config(page_title="Debug", layout="wide")

st.title("🔍 Отладка подключения к Google Sheets")

# 1. Проверка secrets
st.header("1. Настройки Secrets")
try:
    spreadsheet_url = st.secrets["connections"]["gsheets"]["spreadsheet"]
    st.success(f"✅ URL таблицы найден: `{spreadsheet_url[:60]}...`")
except Exception as e:
    st.error(f"❌ Не найден URL таблицы: {e}")
    st.stop()

try:
    creds_dict = dict(st.secrets["connections"]["gsheets"]["credentials"])
    st.success("✅ Словарь credentials получен")
    st.write("**Поля в credentials:**")
    for key in creds_dict.keys():
        if key == "private_key":
            st.write(f"- `{key}`: `{creds_dict[key][:40]}...` (обрезано)")
        else:
            st.write(f"- `{key}`: `{creds_dict[key]}`")
except Exception as e:
    st.error(f"❌ Ошибка в credentials: {e}")
    st.stop()

# 2. Проверка private_key
st.header("2. Формат private_key")
pk = creds_dict.get("private_key", "")
if "BEGIN PRIVATE KEY" in pk and "END PRIVATE KEY" in pk:
    st.success("✅ Приватный ключ содержит BEGIN и END")
else:
    st.error("❌ Приватный ключ не содержит BEGIN/END — проверьте формат!")
    
# Проверяем, есть ли реальные переносы строк вместо \n
if "\n" in pk and "\\n" not in pk:
    st.warning("⚠️ В ключе РЕАЛЬНЫЕ переносы строк. В Streamlit Secrets это нормально, но проверьте, что ключ был ОДНОЙ строкой при вставке.")
st.write(f"Длина ключа: **{len(pk)}** символов")

# 3. Попытка подключения
st.header("3. Подключение к Google Sheets")
try:
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]
    creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)
    st.success("✅ Credentials созданы")
    
    client = gspread.authorize(creds)
    st.success("✅ Клиент gspread авторизован")
    
    sheet = client.open_by_url(spreadsheet_url)
    st.success(f"✅ Таблица открыта: **{sheet.title}**")
    st.write(f"Листов в таблице: **{len(sheet.worksheets())}**")
    for ws in sheet.worksheets():
        st.write(f"- `{ws.title}` (строк: {ws.row_count}, колонок: {ws.col_count})")
    
    worksheet = sheet.sheet1
    st.success(f"✅ Первый лист: `{worksheet.title}`")
    
    # 4. Пробная запись
    st.header("4. Пробная запись")
    if st.button("🧪 Записать тестовую строку"):
        try:
            test_row = [
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "ТЕСТ", "ТЕСТ", "ТЕСТ", "ТЕСТ", "ТЕСТ", "ТЕСТ"
            ]
            worksheet.append_row(test_row, value_input_option="USER_ENTERED")
            st.success("✅ Тестовая строка записана! Проверьте таблицу.")
        except Exception as e:
            st.error(f"❌ Ошибка записи: {e}")
    
    st.header("5. Чтение данных")
    if st.button("📖 Прочитать данные"):
        try:
            data = worksheet.get_all_records()
            st.write(f"Прочитано строк: **{len(data)}**")
            st.dataframe(pd.DataFrame(data))
        except Exception as e:
            st.error(f"❌ Ошибка чтения: {e}")

except gspread.exceptions.SpreadsheetNotFound:
    st.error("❌ **SpreadsheetNotFound** — таблица не найдена.")
    st.info("Проверьте: 1) URL правильный? 2) Таблица расшарена на email сервисного аккаунта с правами Редактор?")
    st.write(f"Email сервисного аккаунта: `{creds_dict.get('client_email', 'не найден')}`")
except gspread.exceptions.APIError as e:
    st.error(f"❌ **APIError**: {e}")
    st.info("Проверьте, что Google Sheets API и Google Drive API включены в вашем проекте на console.cloud.google.com")
except Exception as e:
    st.error(f"❌ **Общая ошибка**: {type(e).__name__}: {e}")
    st.info("Пришлите скриншот этой ошибки — разберёмся.")
