from django.contrib import admin
from django.urls import path , include 
from Core_Application import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="index"),
    path("contribators/",views.contribators,name="contribators"),
    path("About/",views.About,name="About"),
    path("Join/",views.Join,name="Join"),\
    #path("\Contact",views.Contact,name="Contact"),
    path("Donate/",views.Donate,name="Donate"),
    path("Volunteer/",views.Be_a_Volunteer,name="Volunteer"),
    #("\Events",views.Events,name="Events"),

]