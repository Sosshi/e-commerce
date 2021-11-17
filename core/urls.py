from django.urls import path
from .views import HomePage, ContactPage, SignUpView

urlpatterns = [
    path("", HomePage.as_view(), name="home"),
    path("contact", ContactPage.as_view(), name="contact"),
    path("signup/", SignUpView.as_view(), name="signup"),
]
