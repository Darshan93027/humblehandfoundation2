from django.shortcuts import render
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

import os
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from google.oauth2 import id_token
from google.auth.transport import requests
#from .models import User

def index(req):
    return render(req,"Core_Application/index.html")

def contribators(req):
    return render(req,"Core_Application/contributors.html")
def Join(req):
    return render(req,"Core_Application/join.html")

def About(req):
    return render(req,"Core_Application/about.html")
    
def Donate(req):
    return render(req,"Core_Application/Donate.html")

def Be_a_Volunteer(req):
    return render(req,"Core_Application/be_a_volunteer.html")

def Contact(req):
    return render(req,"Core_Application/contact.html")

def Events(req):
    return render(req,"Core_Application/events.html")

def galleries(req):
    return render(req,"Core_Application/gallery.html")

"""def Message_Sent_Successfully(req):
    if req.method == "POST":
        name = req.POST.get("name")
        email = req.POST.get("email")
        msg = req.POST.get("message")  # Ensure the name in the form matches here
        # Save data to the model
        time = datetime.datetime.now()
        # Format the date as dd/mm/yyyy
        date = time.strftime("%d/%m/%Y")
        # Format the time as 12-hour format with AM/PM
        formatted_time = time.strftime("%I:%M %p")  # %I for 12-hour format, %M for minutes, %p for AM/PM

        datas = volunteer(name=name, email=email, msg=msg, time=formatted_time, date=date)  # Adjust fields if necessary
        datas.save()
        with open("Data.txt", "a") as file:
            file.write(f" {name}       {email}               {msg}                 {formatted_time}    {date}\n")
       
        return render(req, "Core_Application/Message_Sent_Successfully.html")  #
    return render(req, "Core_Application/join.html")  """
 # Replace with the actual model name if different

"""def Message_Sent_Successfully(req):
    if req.method == "POST":
        # Retrieve data from the form
        name = req.POST.get("name")
        email = req.POST.get("email")
        msg = req.POST.get("message")  # Ensure the field name matches the form

        # Save data to the model
        time = datetime.datetime.now()
        date = time.strftime("%d/%m/%Y")  # Format the date as dd/mm/yyyy
        formatted_time = time.strftime("%I:%M %p")  # 12-hour format with AM/PM

        # Save the data into the database
        datas = volunteer(name=name, email=email, msg=msg, time=formatted_time, date=date)  # Adjust fields if necessary
        datas.save()

        # Save the data into a text file
        with open("Data.txt", "a") as file:
            file.write(f"{name}       {email}               {msg}                 {formatted_time}    {date}\n")

        # Send email to the specified email address
        recipient_email = email
        subject = "Thank You for Visiting! HumbleHandFoundation"
        message = (
    f"Dear {name},\n\n"
    "We hope this email finds you well. Thank you for taking the time to visit HumbleHandFoundation. "
    "Your interest in our mission truly inspires us to keep moving forward.\n\n"
    "At HumbleHandFoundation , we are dedicated to making a significant difference in the lives of underprivileged children. "
    "Your support can help provide education, healthcare, and opportunities to those who need them most. "
    "Together, we can give them a brighter future.\n\n"
    "If you would like to contribute, please consider donating today. Even the smallest amount can have a lasting impact. "
    "Visit the link below to learn more and make a donation:\n"
    "**Donate Now**: https://www.example.com/donate\n\n"
    "Thank you once again for your kindness and support. Together, we can change lives and bring smiles to countless children.\n\n"
    "Warm regards,\n\n"
    f"Date: {date}\nTime: {formatted_time}"
)

 
        f"\nDate: {date}\nTime: {formatted_time}"
        from_email = settings.EMAIL_HOST_USER
        
        try:
            send_mail(subject, message, from_email, [recipient_email])
            email_response = "Email sent successfully"
        except Exception as e:
            email_response = f"Failed to send email: {e}"

        # Render the success page
        return render(req, "Core_Application/Message_Sent_Successfully.html", {"email_response": email_response})

    # If not a POST request, return the join page
    return render(req, "Core_Application/join.html")"""

from django.core.mail import EmailMessage
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from reportlab.pdfgen import canvas
import datetime
import os

def generate_pdf(file_path, name, date, time):
   pass
def Message_Sent_Successfully(req):
    if req.method == "POST":
        # Retrieve data from the form
        name = req.POST.get("name")
        email = req.POST.get("email")
        msg = req.POST.get("message")  # Ensure the field name matches the form

        # Save data to the model
        time = datetime.datetime.now()
        date = time.strftime("%d/%m/%Y")  # Format the date as dd/mm/yyyy
        formatted_time = time.strftime("%I:%M %p")  # 12-hour format with AM/PM

        # Save the data into the database
        datas = volunteer(name=name, email=email, msg=msg, time=formatted_time, date=date)  # Adjust fields if necessary
        datas.save()

        # Save the data into a text file
        with open("Data.txt", "a") as file:
            file.write(f"{name}       {email}               {msg}                 {formatted_time}    {date}\n")

        # Email details
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
            "Warm regards,\n\n"
            f"Date: {date}\nTime: {formatted_time}"
        )

        from_email = settings.EMAIL_HOST_USER

        # Path to the PDF file
        pdf_file_path = f"thank_you_{name}.pdf"  # Unique file name for the PDF

        # Generate the PDF if it doesn't exist
        if not os.path.exists(pdf_file_path):
            generate_pdf(pdf_file_path, name, date, formatted_time)

        try:
            # Create an EmailMessage object
            email_message = EmailMessage(subject, message, from_email, [email])

            # Attach the PDF file
            with open(pdf_file_path, 'rb') as pdf_file:
                email_message.attach("Thank_You.pdf", pdf_file.read(), 'application/pdf')

            # Send the email
            email_message.send(fail_silently=False)
            email_response = "Email with PDF sent successfully"
        except Exception as e:
            email_response = f"Failed to send email: {e}"

        # Render the success page
        return render(req, "Core_Application/Message_Sent_Successfully.html", {"email_response": email_response})

    # If not a POST request, return the join page
    return render(req, "Core_Application/join.html")



def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        # Check if username already exists
        if Signup.objects.filter(username=username).exists():
            return render(request, 'Core_Application/signup.html', {'error': 'Username already taken!'})

        # Save new user
        user = Signup(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
        user.save()
        return redirect('login')  # Redirect to login page after signup

    return render(request, 'CoreApplicationsignup.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Check if user exists in Signup table
        try:
            user = Signup.objects.get(username=username, password=password)
            return render(request, 'Core_Application/dashboard.html', {'user': user})  # Redirect to dashboard
        except Signup.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid username or password!'})

    return render(request, 'login.html')