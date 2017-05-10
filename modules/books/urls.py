from django.conf.urls import url
from django.contrib import admin
from .views import ListBook, DetailBook,UploadFiles

urlpatterns = [
    url(r'^$', ListBook.as_view(), name='list-books'),
    url(r'^(?P<pk>[0-9]+)/$', DetailBook.as_view(), name='details-books'),
    url(r'^files/$', UploadFiles.as_view()),
]
