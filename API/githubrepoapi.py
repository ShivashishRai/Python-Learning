

import requests

response = requests.get('https://api.github.com/user', auth=('shivashishrai926@gmail.com','iPhone@14plus'))
response_github_json = response.json()
print(response_github_json)
print(response.status_code)
