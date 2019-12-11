from obratka import *
from pprint import pprint

def get_all__users_rating(url):
    json_obj = json.loads(requests.get(url).content)
    return json_obj

users_rating = get_all__users_rating('http://127.0.0.1:8000/hello/users/ratings/')

def get_users():
    global users_rating

    user__rating = {}
    __users = []

    for user in users_rating:
        
        user__rating ={
            'user_id' : user['user_id'] ,
            'profession' : user['profession'] , 
            'university_name' : user['university_name'] ,
            'university_rating' : user['university_rating']
        }

        __users.append(user__rating)
    
    return __users

__users = get_users()

def devide_by_profession(profession):
    global __users

    devided_array = []

    for user in __users:

        if user['profession'] == profession:
            devided_array.append(user)
    
    return devided_array

def get_profession_names():
    global all__profession
    names = []
    for profession in all__profession:
        names.append(profession['prof_title'])
    names = list(set(names))
    return names

pprint(len(devide_by_profession('Computer science')))
pprint(devide_by_profession('Computer science'))
# pprint(get_profession_names())