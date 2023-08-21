from django.contrib import admin
from django.urls import path,include
from .views import *
from .import views
urlpatterns = [
    # User can fetch(GET),add(POST),update(PATCH),delete(DELETE) the data using this single url 'IMDB_api/'
    path('IMDB_api/',IMDB_API.as_view()),
    path('reviews/', Review.as_view(), name='review-list'),
    path('create_review/', views.createReview, name='create_reviews'),
]