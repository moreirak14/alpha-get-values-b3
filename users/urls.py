from django.urls import path

from .api import RegisterView, RetrieveUserView

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("me/", RetrieveUserView.as_view()),
]
