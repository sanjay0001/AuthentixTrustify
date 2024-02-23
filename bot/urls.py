from django.urls import path
from .views import HomeView,RedirectLogin

urlpatterns=[
    path('',HomeView.as_view(),name="home"),
    path('login_redirect/',RedirectLogin.as_view())
]