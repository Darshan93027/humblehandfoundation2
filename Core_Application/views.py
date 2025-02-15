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

        # Save to database
        volunteer_data = volunteer(
            name=name,
            email=email,
            msg=msg,
            time=formatted_time,
            date=date
        )
        volunteer_data.save()

        # Email content
        subject = "Thank You for Visiting! HumbleHandFoundation"
        message = (
            f"Dear {name},\n\n"
            "We hope this email finds you well. Thank you for taking the time to visit HumbleHandFoundation. "
            "Your interest in our mission truly inspires us to keep moving forward.\n\n"
            "At HumbleHandFoundation, we are dedicated to making a significant difference in the lives of underprivileged children. "
            "Your support can help provide education, healthcare, and opportunities to those who need them most. "
            "Together, we can give them a brighter future.\n\n"
            "If you would like to contribute, please consider donating today. Even the smallest amount can have a lasting impact. "
            "Visit the link below to learn more and make a donation:\n"
            "**Donate Now**: https://www.example.com/donate\n\n"
            "Thank you once again for your kindness and support. Together, we can change lives and bring smiles to countless children.\n\n"
            "Warm regards,\n"
            "HumbleHandFoundation\n\n"
            f"Date: {date}\nTime: {formatted_time}"
        )

        # Email sending
        try:
            email_message = EmailMessage(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [email]
            )

            pdf_file_path = f"thank_you_{name}.pdf"
            if not os.path.exists(pdf_file_path):
                generate_pdf(pdf_file_path, name, date, formatted_time)

            with open(pdf_file_path, 'rb') as pdf_file:
                email_message.attach("Thank_You.pdf", pdf_file.read(), 'application/pdf')

            email_message.send(fail_silently=False)
            email_response = "Email with PDF sent successfully"
        except Exception as e:
            email_response = f"Failed to send email: {str(e)}"

        return render(request, "Core_Application/message_sent_successfully.html", {
            "email_response": email_response
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
    context = {
        'total_donated': '10,000',  # Replace with actual data from your database
        'donations_count': '5',     # Replace with actual data
        'impact_made': '25'         # Replace with actual data
    }
    return render(request, 'Core_Application/dashboard.html', context)

def process_donation(request):
    if request.method == 'POST':
        amount = request.POST.get('custom_amount')
        # Process the donation here
        # Add your payment gateway integration
        return redirect('donation_success')
    return redirect('dashboard')