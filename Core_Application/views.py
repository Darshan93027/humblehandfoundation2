from django.shortcuts import render
from django.http import HttpResponse



def index(req):
    return render(req,"Core_Application/index.html")

def contribators(req):
    return render(req,"Core_Application/contributors.html")
def Join(req):
    return render(req,"Core_Application/join.html")
def About(req):
    return render(req,"Core_Application/about.html")
    
def Donate(req):
    return render(req,"Core_Application/donate.html")

def Be_a_Volunteer(req):
    return render(req,"Core_Application/be_a_volunteer.html")

