from django.shortcuts import render,redirect
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
import os
from dotenv import load_dotenv
load_dotenv()


class HomeView(LoginRequiredMixin,APIView):
    login_url = 'login_redirect/'
    def get(self,request):
        print("HOme is available")
        return Response({"status":"success","message":"Home page is available"})


class RedirectLogin(APIView):
    def get(self,request):
        FRONTEND_URL = os.getenv("FRONTEND_URL")
        print("redirected")
        print(FRONTEND_URL+"login/")
        return redirect(FRONTEND_URL+"login/")