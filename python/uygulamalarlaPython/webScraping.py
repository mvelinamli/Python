import requests
from bs4 import BeautifulSoup

#   Web sayfasının url'i 

url = "https://github.com"

#   Web sayfasına GET isteği gönderme

response = requests.get(url)

#   İsteğin başarılı olup olmadığını kontrol etme

if response.status_code == 200:
    # HTML içeriğini analiz etmek için BeautifulSoup kullanma
    soup = BeautifulSoup(response.content, 'html.parser')

    # İlgili veriyi çıkarma
    title = soup.find('title').text

    # Veriyi yazdırma
    print("Başlık:", title)

else:
    print("Hata! Sayfa yüklenemedi.")
