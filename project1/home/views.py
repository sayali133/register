from django import contrib
from django.shortcuts import redirect, render, HttpResponse
from datetime import datetime
from firebase import firebase
from requests import post, get
from firebase.firebase import FirebaseApplication, FirebaseAuthentication
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import SESSION_KEY, authenticate
from django.contrib.auth import logout, login
import pyrebase
from pyrebase.pyrebase import Database
import firebase_admin
from firebase_admin import credentials


# database connection
config = {
   "apiKey": "AIzaSyBpOXDEEyrhISOB9rMACJWTVXN606X8_1g",
  "authDomain": "event-management-3e192.firebaseapp.com",
  "projectId": "event-management-3e192",
  "storageBucket": "event-management-3e192.appspot.com",
  "messagingSenderId": "336292328707",
  "appId": "1:336292328707:web:1f5e73e746f60034166536",
  "measurementId": "G-KM5WTNRC33",
  "databaseURL":"https://event-management-3e192-default-rtdb.firebaseio.com/",
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()
# cred = credentials.Certificate(
#     'sktrail-c3fea-firebase-adminsdk-attkx-0198865b65.json')
cred = credentials.Certificate('event-management-3e192-firebase-adminsdk-9yioh-d4ef1b4bdd.json')
# firebase_admin.initialize_app(cred)

firebase_admin.initialize_app(cred)


def index(request):
    return render(request, 'index.html')


def postsubmit(request):

    data={
            'Name': request.POST.get('name'),
            'contact' :request.POST.get('contact'),
            'event' : request.POST.get('event'),
            'City' :request.POST.get('City'),
            'Budget' : request.POST.get('Budget'),
            'Guests' : request.POST.get('guests'),
            'Date' : request.POST.get('date'),
    }

    


    database.child("Data").child("Events").push(data)

    msg = "successfully registered Event! ok"
    return render(request, 'index.html', {"msg": msg})
