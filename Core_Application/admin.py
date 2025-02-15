from django.contrib import admin
from Core_Application.models import volunteer,Signup# Import the Volunteer model correctly


#admin.site.register(User)
admin.site.register(volunteer)  # Register the Volunteer model with the admin site
admin.site.register(Signup) # Register the