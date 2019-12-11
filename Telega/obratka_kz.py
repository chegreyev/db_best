import requests
import json 

# Just fot debugging
from pprint import pprint

# Local urls for each DB table 
# Each of them have Rest api {json}
city_url = 'http://127.0.0.1:8000/kz/city/'
professions_url = 'http://127.0.0.1:8000/kz/professions/'
universities_url = 'http://127.0.0.1:8000/kz/university/'
users_url = 'http://127.0.0.1:8000/kz/users/'
users_rating_url = 'http://127.0.0.1:8000/kz/users/ratings/'

# Getting the responce of the each table 
responce_prof = requests.get(professions_url)
responce_univer = requests.get(universities_url)
responce_city = requests.get(city_url)

# Converting the responces to the json object 
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
# Sorts all cities by profession
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
# Sorts all universities by professions
def getUniversityByCity(city):
    global all__cities

    universities = []

    for gorod in all__cities:
        if city == gorod['city_name'] :
            for uni in gorod['universities']:
                universities.append(uni['university_name'])
    
    return universities
# Collecting all first subjects of ENT exam
def getFirstSubjects():
    global all__profession

    first_subjects = []

    for prof in all__profession:
        first_subjects.append(prof['first_lesson'])

    first_subjects = list(set(first_subjects))
    return first_subjects
# Collecting all second subjects related to first subject
def getSecondSubjects(first):
    global all__profession

    second_subjects = []

    for prof in all__profession:
        if first == prof['first_lesson']:
            second_subjects.append(prof['second_lesson'])

    second_subjects = list(set(second_subjects))
    return second_subjects
# Getting all information about chosen university
def getUniversityInfo(university):
    global all__university

    info = ''
    for univer in all__university:
        if univer['university_name'] == university:
            info += '🔢Code of University: ' + str(univer['university_code'])
            info += '\n🆒' + univer['university_name']
            info += '\n✅' + 'Category of University: ' + univer['university_category']
            info += '\n🛑' + 'Type of University: ' + univer['university_type']
            info += '\n📑' + 'Military department: ' + univer['military_dep']
            info += '\n🗳' + 'Official website: ' + univer['university_site']
            info += '\n📬' + 'Official email address: ' + univer['university_email']

    return info
# Posting info to DB
def registerUser(user_id , user_login , password):
    global users_url

    data = {
        'user_id': user_id ,
        'user_login' : user_login ,
        'password' : password
    }

    requests.post(users_url , data)
# Register data for rating the University
def registerUserRating(user_id , profession , universitie_name , university_rating):
    global users_rating_url

    data = {
        'user_id' : user_id , 
        'profession' : profession , 
        'university_name' : universitie_name , 
        'university_rating' : university_rating
    }

    requests.post(users_rating_url , data)

# --------------------DEBUG--------------------
# print(getCitiesByProfession('Computer Engineering and Software'))
# print(getProfessionsBySubjects('Maths' , 'Physics' )) 
# print(getUniversityByProfession('Computer Engineering and Software'))
# print(getUniversityByCity('Atyrau'))

