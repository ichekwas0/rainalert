import requests
from twilio.rest import Client

API_KEY = "32cb88ec8f2495bb47f1e8f3338dc5db"
account_sid = "AC4b8e29a556acf61eaa57b428f44d0805"
auth_token = "e811c0c1cb79ed5e8331a735857c2896"

MY_LAT = 32.776665
MY_LONG = -96.796989


parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "daily,current,minutely"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False
for hour_data in data["hourly"][:12]:
    for weather in hour_data["weather"]:
        if weather["id"] < 700:
            will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain, please bring an umbrella",
        from_='+19106019171',
        to='6825533300'
    )

