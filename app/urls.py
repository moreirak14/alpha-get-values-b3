from django.urls import path

from .api import GetValuesApi

urlpatterns = [
    path("get-values", GetValuesApi.as_view()),
]
