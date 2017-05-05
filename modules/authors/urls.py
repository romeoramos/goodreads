from django.conf.urls import url
from django.contrib import admin
from .views import ListAuthor

urlpatterns = [
    url(r'^$', ListAuthor.as_view()),
]
