import requests

api_key = "5796abbde9106b7da4febfae8c44c232"
city = input("Enter city name: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code==200:
    data = response.json()
    description = data['weather'][0]['description']
    print(f"Weather in {city}: {description}")