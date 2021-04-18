import requests

response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
response.encoding = 'utf-8' # Optional: requests infers this internally
print(type(response))
print(dir(response))
