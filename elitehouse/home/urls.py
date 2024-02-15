from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('error/', err, name='error'),
    path('contact/', contact, name='contact'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('property-list/', property_list, name='property-list'),
    path('property-type/', property_type, name='property-type'),
    path('property-agent/', property_agent, name='property-agent'),
    path('testimonial/', testimonial, name='testimonial'),
    path('about/', about, name='about'),
]
