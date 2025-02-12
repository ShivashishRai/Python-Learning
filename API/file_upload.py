
#Uploading a files through API Call

import requests

se = requests.session()
se.auth = auth={'username':'password'}
url = ''
se.headers = {'content_type':'Application_json'}

files = {'file': open('Excel_Runner.xlsx','rb')}
response = se.get(url,files=files)

response_json = response.json()
print(response.status_code)
print(type(response_json))