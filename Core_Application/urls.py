from django.contrib import admin
from django.urls import path , include 
from Core_Application import views
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns = [
   
    path("",views.index,name="index"),
    path("contribators/",views.contribators,name="contribators"),
    path("About/",views.About,name="About"),
    path("Join/",views.Join,name="Join"),
    path("Contact",views.Contact,name="Contact"),
    path("Donate/",views.Donate,name="Donate"),
    path("Volunteer/",views.Be_a_Volunteer,name="Volunteer"),
    path("Events/",views.Events,name="event"),
    path("Events/",views.galleries,name="gallery"),
    path("Message_Sent_Successfully/",views.Message_Sent_Successfully,name="Message_Sent_Successfully"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)