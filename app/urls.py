from django.urls import path

from .api import GetAlphaVantageApi

urlpatterns = [
    path("get-alpha/", GetAlphaVantageApi.as_view()),
]
