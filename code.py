import pandas as pd
import json
import csv
from google.oauth2 import service_account
import pygsheets

with open('..\\client_secret.json') as source:
    info = json.load(source)
credentials = service_account.Credentials.from_service_account_info(info)

client = pygsheets.authorize(service_account_file='..\\client_secret.json')
sp_url='' #enter spreadsheet url
sheet_data = client.sheet.get("") #enter the sheet id from sp_url
sheet=client.open_by_url(sp_url).sheet1

#print(wks.cols,wks.rows)
df = pd.read_csv(filename+".csv", #filename=which file you want to export to gsheet
                  
                 encoding='utf-8')

#df.drop(columns=['#'], inplace=True)
sheet.set_dataframe(df, start=(1,1),extend=True)
