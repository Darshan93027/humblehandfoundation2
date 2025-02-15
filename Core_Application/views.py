from django.shortcuts import render, redirect
from django.http import HttpResponse
from Core_Application.models import volunteer
import datetime
import time
import pandas as pd

from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
import datetime
from .models import volunteer 


from django.core.mail import EmailMessage
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from reportlab.pdfgen import canvas
import datetime
import os

import os
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from google.oauth2 import id_token
from google.auth.transport import requests
from .models import Signup
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from .tasks import save_volunteer_data, send_thank_you_email

def index(request):
    return render(request, "Core_Application/index.html")

def contribators(request):
    return render(request, "Core_Application/contributors.html")

def join(request):
    return render(request, "Core_Application/join.html")

def about(request):
    return render(request, "Core_Application/about.html")
    
def donate(request):
    return render(request, "Core_Application/donate.html")

def be_a_volunteer(request):
    return render(request, "Core_Application/be_a_volunteer.html")

def contact(request):
    return render(request, "Core_Application/contact.html")

def events(request):
    return render(request, "Core_Application/events.html")

def galleries(request):
    return render(request, "Core_Application/gallery.html")

def generate_pdf(file_path, name, date, time):
    # Implement your PDF generation logic here
    pass

def message_sent_successfully(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        msg = request.POST.get("message")

        current_time = datetime.datetime.now()
        date = current_time.strftime("%d/%m/%Y")
        formatted_time = current_time.strftime("%I:%M %p")

        # Queue tasks and redirect immediately
        try:
            # Queue Celery tasks asynchronously
            save_volunteer_data.apply_async(
                args=[name, email, msg, formatted_time, date],
                countdown=1  # 1 second delay to ensure smooth redirect
            )
            send_thank_you_email.apply_async(
                args=[name, email, date, formatted_time],
                countdown=2  # 2 second delay to ensure data is saved first
            )
        except Exception as e:
            # Log the error but don't wait  
            print(f"Task queuing error: {str(e)}")

        # Redirect immediately with a flash message
        return render(request, "Core_Application/message_sent_successfully.html", {
            "email_response": "Thank you! Your message is being processed.",
            "debug_info": {
                "name": name,
                "email": email,
                "date": date,
                "time": formatted_time
            }
        })

    return render(request, "Core_Application/join.html")

def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if Signup.objects.filter(username=username).exists():
            return render(request, 'Core_Application/signup.html', {
                'error': 'Username already taken!'
            })

        # Hash password before saving
        hashed_password = make_password(password)
        user = Signup(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=hashed_password
        )
        user.save()
        return redirect('login')

    return render(request, 'Core_Application/signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = Signup.objects.get(username=username)
            if check_password(password, user.password):
                return render(request, 'Core_Application/dashboard.html', {'user': user})
            else:
                raise Signup.DoesNotExist
        except Signup.DoesNotExist:
            return render(request, 'Core_Application/login.html', {
                'error': 'Invalid username or password!'
            })

    return render(request, 'Core_Application/login.html')

@login_required
def dashboard(request):
    
    return render(request, 'Core_Application/dashboard.html', )

def process_donation(request):
    if request.method == 'POST':
        amount = request.POST.get('custom_amount')
        # Process the donation here
        # Add your payment gateway integration
        return redirect('donation_success')
    return redirect('dashboard')