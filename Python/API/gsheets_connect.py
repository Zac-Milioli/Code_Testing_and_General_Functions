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