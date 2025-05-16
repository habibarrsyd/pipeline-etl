import pandas as pd
from utils.load import save_to_csv, save_to_google_sheets
import os

def test_save_to_csv(tmp_path):
    df = pd.DataFrame({"title": ["Test Product"], "price": [160000.0]})
    file_path = tmp_path / "test_output.csv"
    save_to_csv(df, str(file_path))
    assert file_path.exists()
    df_read = pd.read_csv(file_path)
    assert not df_read.empty
    assert df_read["title"].iloc[0] == "Test Product"

# Catatan: Tes untuk save_to_google_sheets sulit dijalankan lokal tanpa setup autentikasi penuh,
# jadi kita skip tes ini atau gunakan mock untuk simulasi (opsional).
def test_save_to_google_sheets_mock(mocker):
    df = pd.DataFrame({"title": ["Test Product"], "price": [160000.0]})
    mocker.patch("googleapiclient.discovery.build")
    save_to_google_sheets(df, "test_spreadsheet_id")
    assert True  # Hanya cek apakah fungsi berjalan tanpa error