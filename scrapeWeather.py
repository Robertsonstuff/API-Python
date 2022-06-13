
import requests


your_key = #put your authentication key here. You get this from your API platform that you use.
r = requests.get('http://api.weatherapi.com/v1/current.json?key={your_key}')

data = r.json()

print(f" The weather in {data['location']['name']}")
print(f" at {data['location']['localtime']}")
print(f" is {data['current']['temp_c']}")


# what my data gave me the following. Note the nested structure.
# this will help you parse the data you want.
# {"location":
    {"name":"New York",
#       "region":"New York",
#       "country":"United States of America",
#       "lat":40.71,
#       "lon":-74.01,
#       "tz_id":"America/New_York",
#       "localtime_epoch":1655143188,
#       "localtime":"2022-06-13 13:59"},
#"current":
    {"last_updated_epoch":1655142300,
#       "last_updated":"2022-06-13 13:45",
#       "temp_c":28.3,
#       "temp_f":82.9,
#       "is_day":1,
}
