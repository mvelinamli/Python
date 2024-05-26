import requests

def weather_forecast(location):
    api_key = 'bdfbb923f8816c03178e3356cf51508b'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()

    if data['cod'] == '404':
        print("Konum bulunamadı. Lütfen geçerli bir konum girin.")
    
    weather_forecast_info = data['weather'][0]['description']
    temperature = data['main']['temp']
    humidity_level = data['main']['humidity']

    print(f"{location} için hava durumu:")
    print(f"Hava: {weather_forecast_info}")
    print(f"Sıcaklık: {temperature} derece")
    print(f"Nem Oranı: {humidity_level}%")

def main():
    location = input("Hava durumu öğrenmek istediğiniz şehri veya ülkeyi girin: ")
    weather_forecast(location)

if __name__ == "__main__":
    main()
