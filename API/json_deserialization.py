
import json

#Loding the json dara file into an object
data_load = open('C:\\Users\\shiva\\PycharmProjects\\GfGpythonLearning\\API\\json_data','rb')
my_json = json.load(data_load)

#fetching json parser string
print(my_json['labs'][3]['time'])
print(my_json['imaging'][1]['location'])
print(type(my_json))