import json
import requests
import pprint

city = 'shenzhen'
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=' + city + '&cnt=3&appid=877d2c132d8c28efc7e43ea4fdd98310'
res = requests.get(url)
res.raise_for_status()
weatherData = json.loads(res.text)

w = weatherData['list']

print('Current weather in %s:' % city)
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
