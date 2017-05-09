from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^authors/', include("modules.authors.urls")),
    url(r'^books/', include("modules.books.urls")),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

]
