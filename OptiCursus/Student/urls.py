from .views import Preferences, CVHandler, WebScrapper
from django.urls import path

app_name = "student"

url_paterns = [
    path('Preferences/', Preferences, name="PreferenceData"),
    path('CVHandler/', CVHandler, name="CV"),
    path('WebScrapper/', WebScrapper, name="WebScrap"),
]