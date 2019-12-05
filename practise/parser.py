import requests
import json

url = 'http://127.0.0.1:8000/hello/city/'

responce = requests.get(url)
def get_all():
    json_obj = json.loads(responce.content)
    return json_obj

all = get_all()

for i in all:
    universities = i['location'][0]['university_name']
    print(universities)