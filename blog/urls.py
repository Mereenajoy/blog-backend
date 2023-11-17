from django.urls import path , include
from . import views

urlpatterns = [
    path('add/',views.addPost , name='add' ),
    path('view/',views.viewPost , name='view' ),
    path('search/',views.searchPost , name='search' ),


]
