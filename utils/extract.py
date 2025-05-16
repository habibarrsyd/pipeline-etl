import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def scrape_main():
    try:
        data = []
        for page in range(1, 51):  # Halaman 1 sampai 50
            url = f"https://fashion-studio.dicoding.dev/?page={page}"
            print(f"Scraping page {page}: {url}")
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124"}
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Cari semua produk dengan class 'product-details'
            products = soup.find_all("div", class_="product-details")
            print(f"Found {len(products)} products on page {page}")
            
            for product in products:
                # Ekstrak title
                title = product.find("h3", class_="product-title")
                title = title.text.strip() if title else "N/A"
                
                # Ekstrak price
                price_container = product.find("div", class_="price-container")
                price = price_container.find("span", class_="price").text.strip() if price_container and price_container.find("span", class_="price") else "N/A"
                
                # Ekstrak rating, colors, size, gender dari tag <p> dengan style tertentu
                p_tags = product.find_all("p", style="font-size: 14px; color: #777;")
                rating = "N/A"
                colors = "N/A"
                size = "N/A"
                gender = "N/A"
                
                for p in p_tags:
                    text = p.text.strip()
                    if "Rating" in text:
                        rating = text
                    elif "Colors" in text:
                        colors = text
                    elif "Size" in text:
                        size = text
                    elif "Gender" in text:
                        gender = text
                
                item = {
                    "title": title,
                    "price": price,
                    "rating": rating,
                    "colors": colors,
                    "size": size,
                    "gender": gender,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                print("Product data:", item)
                data.append(item)
            
            # Hentikan jika halaman kosong
            if not products:
                print(f"No products on page {page}. Stopping.")
                break
        
        print(f"Total products collected: {len(data)}")
        return pd.DataFrame(data)
    except requests.RequestException as e:
        print(f"Error during scraping: {e}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Unexpected error: {e}")
        return pd.DataFrame()