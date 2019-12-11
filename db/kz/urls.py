from django.urls import path
from .views import *

urlpatterns = [
    path('city/' , CityView.as_view() , name = 'city_list'),
    path('university/' , UniversityView.as_view() , name = 'university_list'),
    path('professions/' , ProfessionView.as_view() , name = 'professions'),
    path('users/' , TUserView.as_view() , name = 'telegram_users'),
    path('users/ratings/' , TUserRatingView.as_view() , name = 'university_rating')

]