
import requests
import json

import configparser

config = configparser.ConfigParser()
config.read('properties.ini')

results = requests.get(config['API']['endpoint']+'/GetBook.php',params={'AuthorName':'Apra'})

# print(results.text)
# result_book = json.loads(results.text)
# print(result_book[0]['isbn'])

response_json = results.json()
print(type(response_json))
print(response_json)
print(results.status_code)
print(results.headers)
print(results.url)