import pandas as pd
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

def save_to_csv(df, file_path="products.csv"):
    try:
        df.to_csv(file_path, index=False)
        print(f"Data saved to {file_path}")
    except Exception as e:
        print(f"Error saving to CSV: {e}")

def save_to_google_sheets(df, spreadsheet_id, credentials_file="google-sheets-api.json"):
    try:
        creds = Credentials.from_service_account_file(credentials_file)
        service = build("sheets", "v4", credentials=creds)
        sheet = service.spreadsheets()
        values = [df.columns.tolist()] + df.values.tolist()
        body = {"values": values}
        sheet.values().update(
            spreadsheetId=spreadsheet_id,
            range="Sheet1!A1",
            valueInputOption="RAW",
            body=body
        ).execute()
        print("Data saved to Google Sheets")
    except Exception as e:
        print(f"Error saving to Google Sheets: {e}")