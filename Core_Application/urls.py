from django.contrib import admin
from django.urls import path, include
from Core_Application import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('contributors/', views.contribators, name='contributors'),
    path('about/', views.about, name='about'),
    path('join/', views.join, name='join'),
    path('contact/', views.contact, name='contact'),
    path('donate/', views.donate, name='donate'),
    path('volunteer/', views.be_a_volunteer, name='volunteer'),
    path('events/', views.events, name='events'),
    path('gallery/', views.galleries, name='gallery'),
    path('message_sent/', views.message_sent_successfully, name='message_sent'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('process-donation/', views.process_donation, name='process_donation'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)