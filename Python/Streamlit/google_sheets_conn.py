# CONEXÃO COM GOOGLE SHEETS VIA STREAMLIT
# IMPORTANTE
# A conexão via GSheetsConnection parece funcionar
# apenas com versões antigas do Streamlit, especificamente 1.29.0

# Próprio do streamlit para fazer query SQL dentro da planilha google sheets ou retorná-la
from streamlit_gsheets import GSheetsConnection
import streamlit as st

conn = st.connection("gsheets", type=GSheetsConnection, ttl=0)
data = conn.read(worksheet='user')
st.dataframe(data, use_container_width=True)


# CONEXÃO DIRETA GOOGLE SHEETS
import gspread
from google.oauth2.service_account import Credentials
import json

credentials = {"credenciais aqui obviamente"}
credentials = json.loads(credentials)
sheet_id = 1234567890
scopes = ["https://www.googleapis.com/auth/spreadsheets"]

creds = Credentials.from_service_account_info(credentials, scopes=scopes)
client = gspread.authorize(creds)

workbook = client.open_by_key(sheet_id)
worksheet = workbook.worksheet('nome da worksheet')

def add_row(values: list):
    worksheet.append_row(values)