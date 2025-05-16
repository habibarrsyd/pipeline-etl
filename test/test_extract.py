import pytest
from unittest.mock import patch
from utils.extract import scrape_main

def test_scrape_main():
    with patch("requests.get") as mocked_get:
        # Simulasi respons HTML sederhana
        mocked_get.return_value.status_code = 200
        mocked_get.return_value.content = """
            <html>
                <div class='product-details'>
                    <h3 class='product-title'>Test Product</h3>
                    <div class='price-container'><span class='price'>$10.00</span></div>
                    <p style='font-size: 14px; color: #777;'>Rating: ★ 4.5 / 5</p>
                    <p style='font-size: 14px; color: #777;'>3 Colors</p>
                    <p style='font-size: 14px; color: #777;'>Size: M</p>
                    <p style='font-size: 14px; color: #777;'>Gender: Men</p>
                </div>
            </html>
        """.encode()
        df = scrape_main()
        assert not df.empty
        assert "title" in df.columns
        assert df["title"].iloc[0] == "Test Product"
        assert "price" in df.columns
        assert "rating" in df.columns
        assert "colors" in df.columns
        assert "size" in df.columns
        assert "gender" in df.columns
        assert "timestamp" in df.columns