from django.conf.urls import url
from django.contrib import admin

from core.views import get_items

urlpatterns = [
    url(r'^get/', get_items)
]