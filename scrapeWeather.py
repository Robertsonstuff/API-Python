from os import name 
import requests

PARAMS = {'location':name}

r = requests.get('http://api.weatherapi.com/v1/current.json?key=f43825f18c2842b0ace175153221306&q=New York&aqi=no', params = PARAMS)

data = r.json()

print(f" The weather in {data['location']['name']}")
print(f" at {data['location']['localtime']}")
print(f" is {data['current']['temp_c']}")

# UQt4rd

# {"location":{"name":"New York",
#   "region":"New York",
#   "country":"United States of America",
#   "lat":40.71,
#   "lon":-74.01,
#   "tz_id":"America/New_York",
#   "localtime_epoch":1655143188,
#   "localtime":"2022-06-13 13:59"},
#"current":{"last_updated_epoch":1655142300,
#"last_updated":"2022-06-13 13:45",
#"temp_c":28.3,
#"temp_f":82.9,
#"is_day":1,
#   "condition":{"text":"Partly cloudy","icon":"//cdn.weatherapi.com/weather/64x64/day/116.png","code":1003},
#"wind_mph":5.6,
# "wind_kph":9.0,
# "wind_degree":310,
# "wind_dir":"NW",
# "pressure_mb":1012.0,
# "pressure_in":29.89,
# "precip_mm":0.0,
# "precip_in":0.0,
# "humidity":48,
# "cloud":75,
# "feelslike_c":28.8,
# "feelslike_f":83.8,
# "vis_km":16.0,
# "vis_miles":9.0,
# "uv":7.0,
# "gust_mph":7.4,
# "gust_kph":11.9}}
