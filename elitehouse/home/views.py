from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views import View
from .models import *

def index(request):
    return render(request, 'index.html')

def err(request):
    return render(request, '404.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def property_list(request):
    return render(request, 'property-list.html')

def property_type(request):
    return render(request, 'property-type.html')

def property_agent(request):
    return render(request, 'property-agent.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def about(request):
    return render(request, 'about.html')

def register(request):
    if request.POST:
        role = request.POST.get('role')
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')
        mobile_no = request.POST.get('mobile')
        dob = request.POST.get('dob')
        state = request.POST.get('state')
        city = request.POST.get('city')
        area = request.POST.get('area')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        prof_pic = request.POST.get('profilePic')
        document = request.POST.get('document')

        # Password fields
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')

        if password != confirm_password:
            # Handle password mismatch error
            return render(request, 'register.html', {'error_message': 'Passwords do not match'})

        # Check the selected role and save the appropriate instance
        if role == 'seller':
            seller = Seller(
                first_name=first_name,
                last_name=last_name,
                email=email,
                mobile_no=mobile_no,
                password=password,
                dob=dob,
                state=state,
                city=city,
                area=area,
                pincode=pincode,
                prof_pic=prof_pic,
                address=address,
                document=document
            )
            seller.save()

        elif role == 'buyer':
            buyer = Buyer(
                first_name=first_name,
                last_name=last_name,
                email=email,
                mobile_no=mobile_no,
                password=password,
                dob=dob,
                state=state,
                city=city,
                area=area,
                pincode=pincode,
                prof_pic=prof_pic,
                address=address
            )
            buyer.save()

        else:
            # Handle invalid role error
            return render(request, 'register.html', {'error_message': 'Invalid role selected'})

        # Redirect to a success page or wherever you want
        return redirect('login')

    return render(request, 'register.html')
