import requests
import json 
from pprint import pprint

city_url = 'http://127.0.0.1:8000/hello/city/'
professions_url = 'http://127.0.0.1:8000/hello/professions/'
universities_url = 'http://127.0.0.1:8000/hello/university/'

responce_prof = requests.get(professions_url)
responce_univer = requests.get(universities_url)
responce_city = requests.get(city_url)

def get_all__profession():
    json_obj = json.loads(responce_prof.content)
    return json_obj

def get_all__univeristy():
    json_obj = json.loads(responce_univer.content)
    return json_obj

def get_all__cities():
    json_obj = json.loads(responce_city.content)
    return json_obj

all__profession = get_all__profession()
all__university = get_all__univeristy()
all__cities = get_all__cities()

# Sorts all professions by 2 ENT Subjects
def getProfessionsBySubjects(first , second):
    global all__profession
    profs = []

    for prof in all__profession:
        if prof['first_lesson'] == first and prof['second_lesson'] == second:
            profs.append(prof['prof_title'])

    profs = list(set(profs))

    return profs

#'Physics' 'Maths'



def getCitiesByProfession(profession):
    global all__cities

    cities = []

    for city in all__cities:
        for univers in city['universities']:
            for profs in univers['professions']:
                if profession == profs['prof_title']:
                    cities.append(city['city_name'])
    
    cities = list(set(cities))
    return cities

def getUniversityByCity(city):
    global all__cities

    universities = []

    for gorod in all__cities:
        if city == gorod['city_name'] :
            for uni in gorod['universities']:
                universities.append(uni['university_name'])
    
    return universities

def getFirstSubjects():
    global all__profession

    first_subjects = []

    for prof in all__profession:
        first_subjects.append(prof['first_lesson'])

    first_subjects = list(set(first_subjects))
    return first_subjects

def getSecondSubjects(first):
    global all__profession

    second_subjects = []

    for prof in all__profession:
        if first == prof['first_lesson']:
            second_subjects.append(prof['second_lesson'])

    second_subjects = list(set(second_subjects))
    return second_subjects



# print(getCitiesByProfession('Computer Engineering and Software'))
# print(getProfessionsBySubjects('Maths' , 'Physics' )) 
# print(getUniversityByProfession('Computer Engineering and Software'))
# print(getUniversityByCity('Atyrau'))

