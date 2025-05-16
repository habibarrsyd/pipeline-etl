import pandas as pd

def transform_data(df):
    try:
        # Hapus duplikat
        df = df.drop_duplicates()

        # Hapus data null
        df = df.dropna()

        # Hapus data invalid
        df = df[df["title"] != "Unknown Product"]
        df = df[df["rating"] != "Rating: ★ Invalid Rating / 5"]
        df = df[df["price"] != "Price Unavailable"]

        # Transformasi kolom Price ke Rupiah (1 USD = Rp16.000)
        def convert_to_rupiah(price_str):
            try:
                # Hapus simbol dolar dan ubah ke float
                price = float(price_str.replace("$", "").strip())
                return price * 16000  # Konversi ke Rupiah
            except (ValueError, AttributeError):
                return None  # Kembalikan None jika konversi gagal

        df["price"] = df["price"].apply(convert_to_rupiah)

        # Transformasi kolom Rating
        df["rating"] = df["rating"].str.extract(r"(\d+\.\d)")[0].astype(float)

        # Transformasi kolom Colors
        df["colors"] = df["colors"].str.replace(" Colors", "", regex=False).astype(int)

        # Transformasi kolom Size
        df["size"] = df["size"].str.replace("Size: ", "", regex=False)

        # Transformasi kolom Gender
        df["gender"] = df["gender"].str.replace("Gender: ", "", regex=False)

        # Pastikan tipe data
        df = df.astype({
            "title": str,
            "price": float,  # Akan menghapus baris dengan None di price
            "rating": float,
            "colors": int,
            "size": str,
            "gender": str,
            "timestamp": str
        })

        # Hapus baris dengan nilai None di kolom price setelah konversi
        df = df.dropna(subset=["price"])

        return df
    except Exception as e:
        print(f"Error during transformation: {e}")
        return pd.DataFrame()