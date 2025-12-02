# Pipeline ETL - Product Data Processing

Pipeline ETL (Extract, Transform, Load) untuk memproses dan membersihkan data produk, kemudian menyimpannya ke CSV dan Google Sheets.

## 📋 Deskripsi

Project ini adalah implementasi pipeline ETL yang dirancang untuk:
- **Extract**: Mengekstrak data produk dari file CSV
- **Transform**: Membersihkan dan mentransformasi data produk
- **Load**: Menyimpan hasil data yang sudah dibersihkan ke CSV dan Google Sheets

## 🛠️ Tech Stack

### Core Technologies
- **Python 3.x** - Bahasa pemrograman utama
- **Pandas 2.2.3** - Library untuk manipulasi dan analisis data
- **NumPy 2.2.5** - Library untuk komputasi numerik

### Google Cloud Integration
- **Google API Python Client 2.152.0** - Client library untuk Google APIs
- **Google Auth 2.36.0** - Library autentikasi Google
- **Google Auth HTTPLib2 0.2.0** - Transport untuk Google Auth
- **Google API Core 2.24.2** - Core library untuk Google API

### Data Processing & Utilities
- **Requests 2.32.3** - HTTP library untuk request data
- **BeautifulSoup4 4.12.3** - Library untuk parsing HTML/XML

### Testing
- **pytest 8.2.0** - Framework testing
- **pytest-mock 3.14.0** - Plugin pytest untuk mocking
- **Coverage 7.6.0** - Tool untuk mengukur code coverage

### Supporting Libraries
- **python-dateutil 2.9.0** - Extension untuk datetime
- **pytz 2025.2** - Timezone definitions
- **colorama 0.4.6** - Cross-platform colored terminal text

## 📁 Struktur Project

```
pipeline-etl/
├── main.py                 # Entry point aplikasi
├── requirements.txt        # Dependencies Python
├── products. csv           # Data produk mentah (input)
├── products_clean.csv     # Data produk yang sudah dibersihkan (output)
├── submissions.txt        # File submission
├── utils/                 # Modul utility
│   ├── extract.py        # Modul untuk ekstraksi data
│   ├── transform.py      # Modul untuk transformasi data
│   └── load.py           # Modul untuk load/simpan data
└── test/                  # Unit tests
    ├── test_extract.py   # Test untuk modul extract
    ├── test_transform.py # Test untuk modul transform
    └── test_load.py      # Test untuk modul load
```

## 🚀 Cara Kerja Pipeline

### 1. Extract (Ekstraksi)
- Membaca data produk dari file `products.csv`
- Validasi data input

### 2. Transform (Transformasi)
- Membersihkan data dari nilai yang tidak valid
- Menghapus data duplikat
- Normalisasi format data
- Filtering data yang tidak sesuai kriteria

### 3. Load (Pemuatan)
- Menyimpan data yang sudah dibersihkan ke file CSV (`products_clean.csv`)
- Mengunggah data ke Google Sheets untuk visualisasi dan sharing

## 📦 Instalasi

1. Clone repository ini:
```bash
git clone https://github.com/habibarrsyd/pipeline-etl.git
cd pipeline-etl
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Setup Google Sheets API:
   - Buat project di Google Cloud Console
   - Enable Google Sheets API
   - Download credentials JSON
   - Simpan credentials di project directory

4. Update Spreadsheet ID di `main.py`:
```python
spreadsheet_id = "YOUR_SPREADSHEET_ID"  # Ganti dengan ID spreadsheet Anda
```

## 💻 Cara Penggunaan

Jalankan pipeline ETL:
```bash
python main.py
```

Output yang dihasilkan:
```
Reading data from CSV...
Starting transformation...
Saving transformed data to CSV...
Saving to Google Sheets...
Process completed. 
```

## 🧪 Testing

Jalankan unit tests:
```bash
pytest
```

Jalankan tests dengan coverage report:
```bash
pytest --cov=utils --cov-report=html
```

## 📊 Input & Output

### Input
- **products.csv**: File CSV berisi data produk mentah yang perlu dibersihkan

### Output
- **products_clean.csv**: File CSV berisi data produk yang sudah dibersihkan dan siap digunakan
- **Google Sheets**: Data otomatis terupload ke spreadsheet untuk akses dan kolaborasi yang mudah

## 🔧 Konfigurasi

Pastikan Anda memiliki:
- File `products.csv` di root directory
- Credentials Google API yang valid
- Spreadsheet ID yang sudah dikonfigurasi

## 📝 Fitur Utama

✅ Automated data cleaning dan transformation  
✅ Dual output (CSV + Google Sheets)  
✅ Error handling yang robust  
✅ Unit testing comprehensive  
✅ Modular architecture untuk maintainability  

## 🤝 Kontribusi

Contributions, issues, dan feature requests sangat diterima! 

## 📄 License

Project ini dibuat untuk keperluan pembelajaran dan development. 

## 👤 Author

**habibarrsyd**
- GitHub: [@habibarrsyd](https://github.com/habibarrsyd)

---

Made with ❤️ using Python & Pandas
```
