import pandas as pd
from utils.transform import transform_data
from utils.load import save_to_csv, save_to_google_sheets

def main():
    # Baca data dari CSV
    print("Reading data from CSV...")
    df = pd.read_csv("products.csv")
    if df.empty:
        print("No data in CSV. Exiting.")
        return
    
    # Transformasi data
    print("Starting transformation...")
    df_clean = transform_data(df)
    if df_clean.empty:
        print("No data after transformation. Exiting.")
        return
    
    # Simpan data bersih ke CSV
    print("Saving transformed data to CSV...")
    save_to_csv(df_clean, "products_clean.csv")
    
    # Simpan data bersih ke Google Sheets
    print("Saving to Google Sheets...")
    spreadsheet_id = "1qoxnlk10TPLrzIpwe21luqdwAfwMjcccpPAMGWy7XJE"  # Ganti dengan ID spreadsheetmu
    save_to_google_sheets(df_clean, spreadsheet_id)
    
    print("Process completed.")

if __name__ == "__main__":
    main()