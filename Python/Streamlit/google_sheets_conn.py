#   IMPORTANTE
# A conexão via GSheetsConnection parece funcionar
# apenas com versões antigas do Streamlit, especificamente 1.29.0

import streamlit as st
# Próprio do streamlit para fazer query SQL dentro da planilha google sheets ou retorná-la
from streamlit_gsheets import GSheetsConnection
# Usado para adicionar dados na planilha
import gspread
from google.oauth2.service_account import Credentials

import json

# ESTA VARIÁVEL É SENSÍVEL E NA APLICAÇÃO REAL DEVE SER ADICIONADA AO ENV DO STREAMLIT E ACESSADA ATRAVÉS DE st.secrets["credentials"]
credentials = {"example": "No auth"}

with open("credentials.json", "w") as file:
    json.dump(credentials, file, indent=2)

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file(r"credentials.json", scopes=scopes)
client = gspread.authorize(creds)
# ESTA VARIÁVEL É SENSÍVEL E NA APLICAÇÃO REAL DEVE SER ADICIONADA AO ENV DO STREAMLIT E ACESSADA ATRAVÉS DE st.secrets["sheet_id"]
sheet_id = "example id"
workbook = client.open_by_key(sheet_id)
worksheet = workbook.worksheet('user')

conn = st.connection("gsheets", type=GSheetsConnection, ttl=5)
data = conn.read(worksheet='user')
st.dataframe(data, use_container_width=True)

name = st.text_input("name")
id_ = st.text_input("id")
text = st.text_input("text")

col1, col2 = st.columns(2)
if col1.button("Adicionar linha nova", use_container_width=True):
    worksheet.append_row([name, id_, text])
if col2.button("Recarregar a página", use_container_width=True):
    st.rerun()