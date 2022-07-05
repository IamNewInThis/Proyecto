from django.urls import path
from .views import *

urlpatterns = [
    path('',root),
    path('home', home,name="home"),
    path('maceteros',maceteros,name="maceteros"),
    path('flores',flores,name="flores"),
    path('tierra',tierra,name="tierra"),
    path('subscripcion',subscripcion,name="subscripcion"),
    path('arbustos',arbustos,name="arbustos")
]