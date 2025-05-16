import pandas as pd
from utils.transform import transform_data

def test_transform_data():
    # Data contoh untuk tes
    df = pd.DataFrame({
        "title": ["Test Product"],
        "price": ["$10.00"],
        "rating": ["Rating: 4.5 / 5"],
        "colors": ["3 Colors"],
        "size": ["Size: M"],
        "gender": ["Gender: Men"],
        "timestamp": ["2025-05-06 12:00:00"]
    })
    
    df_clean = transform_data(df)
    assert not df_clean.empty
    assert df_clean["price"].iloc[0] == 160000.0  # $10.00 * 16000
    assert df_clean["rating"].iloc[0] == 4.5
    assert df_clean["colors"].iloc[0] == 3
    assert df_clean["size"].iloc[0] == "M"
    assert df_clean["gender"].iloc[0] == "Men"
    assert df_clean["timestamp"].iloc[0] == "2025-05-06 12:00:00"