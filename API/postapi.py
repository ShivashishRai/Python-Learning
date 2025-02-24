

import requests
import configparser
from Configurations import *


# my_config=configparser.configparser()
# my_config.read('properties.ini')
# newheaders = {}
# my_json_response = requests.post(my_config['API']['endpoint']+'/Addbook.php', json= ,headers= newheaders )

header = {'Content-Type': "application/json"}
book = {"name": "100 Days Learning", "isbn": "100Day", "aisle": "2878", "author":"PujuRai"}
print("************ADD Book*********************")
config = getconfig()             #Object reference for Get config method
response = requests.post(config['API']['endpoint']+config['Resources']['add_book_resource'], json=book, headers=header)
add_book_response_json = response.json()

print(response.status_code)
print(add_book_response_json)                      # parse the response in the jaon format
print(response.url)
book_id = add_book_response_json['ID']             #Contains the newly added book id

print("************DeleteBook*********************")
#Delete Book
book_to_be_deleted = {"ID": book_id}
response = requests.post(config['API']['endpoint']+config['Resources']['delete_book_resource'], json=book_to_be_deleted, headers=header)
print(type(response))
delete_response_json = response.json()

print(delete_response_json)
assert delete_response_json['msg'] == 'book is successfully deleted'
print(response.status_code)
print(response.url)





