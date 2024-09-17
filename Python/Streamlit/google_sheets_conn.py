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

# Pode ser feito
new_data = conn.query('SELECT * FROM user WHERE age > 30')
st.dataframe(new_data, use_container_width=True)