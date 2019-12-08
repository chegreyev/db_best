import requests
from pprint import pprint
import json

url = 'http://127.0.0.1:8000/hello/city/'

responce = requests.get(url)

def get_all():
    json_obj = json.loads(responce.content)
    return json_obj

all = get_all()

def getCities(data):
    all = data
    cities = []

    for i in data: 
        cities.append(i['city_name'])
    return cities

def getUnivers(city):

    global all
    univers = []
    for i in all:
        if i['city_name'] == city:
            for univer in i['universities']:
                univers.append(univer)

    return univers

def getProfessions(city , university):
    
    universities = getUnivers(city)

    for univer in universities:
        if university == univer['university_name']:
            return univer['professions']


def HUI(city , university , profession):

    professions = getProfessions(city , university)
    subjects = []
    for hui in professions:
        if profession == hui['prof_title']:
            subjects.append(hui['first_lesson'])
            subjects.append(hui['second_lesson'])
    return subjects


# print(HUI('Atyrau' , 'Atyrau State University named after H. Dosmukhamedov' , 'Two Foreighn languages'))