import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random


def get_sheet_data(flag_name):
    # Define the scope and authenticate using the JSON key file
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    # Replace yourjson with your json file name
    creds = ServiceAccountCredentials.from_json_keyfile_name('yourjson.json', scope)
    client = gspread.authorize(creds)

    # Open the spreadsheet and fetch data
    sheet = client.open(f"{flag_name}").sheet1
    data = sheet.col_values(2)[1:]  # Fetches rows in the sheet
    '''Important notice: sheets rows may vary depending on number of replies 
    and sheets cols may vary depending on number of questions.
    Thus col_values(2) is not absolute.'''
    data_filter = [s for s in data if s != ""]

    def data_number_identify():
        if len(data_filter) > 10:
            data_select = random.sample(data_filter, 10)
            return data_select
        elif len(data_filter) <= 0:
            print("리스트 공백")
        else:
            return data_filter

    final_data = data_number_identify()
    print(final_data)
    return final_data
