from django.urls import path
from .views import SignupViewSet,ProfileViewSet
from rest_framework.authtoken.views import ObtainAuthToken


urlpatterns = [
    path("register/", SignupViewSet.as_view(), name="register"),
    path("login/", ObtainAuthToken.as_view(), name="login"),
    path("profile/<str:username>/", ProfileViewSet.as_view(), name="profile"),
]