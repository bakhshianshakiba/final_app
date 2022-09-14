from django.shortcuts import render
from .forms import SignUpCrispy, LoginCrispy, BuyInfoCrispy
from .models import SignUpModel,LoginModel,BuyInfoModel , ContacUstModel

from django import forms
# Create your views here.

def home_view(request):
    return render(request,'index.html',{})

def about(request):
    return render(request,'about.html',{})

def buy(request):
    return render(request,'buy.html',{})

def contact(request):
    # if request.method== "POST":
    #     contact_us = ContactModel()
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     phone_number = request.POST.get('phone_number')
    #     message = request.POST.get('message')
    #
    #     contact_us.name = name
    #     contact_us.email = email
    #     contact_us.phone_number = phone_number
    #     contact_us.message = message
    #     contact_us.save()
    #     return render(request, 'index.html', {})

    return render(request,'contact.html',{})

def medicine(request):
    return render(request,'medicine.html',{})

def news(request):
    return render(request,'news.html',{})

def signup(request):
    context = {'form': SignUpCrispy()}
    context2 = {'form': LoginCrispy()}
    if request.method == 'POST':
        sign_up = SignUpModel()
        name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if SignUpModel.objects.filter(email__iexact=email).exists():
            return render(request, 'exist.html', {})
        else:
            sign_up.name = name
            sign_up.email = email
            sign_up.username = username
            sign_up.password = password
            sign_up.save()
            return render(request, 'login.html', context2)
    return render(request,'signup.html',context)
def login(request):
    context = {'form': LoginCrispy()}
    log_in = LoginModel()
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if SignUpModel.objects.filter(email__iexact=email, password__iexact=password).exists():
            log_in.email = email
            log_in.password = password
            log_in.save()
            return render(request, 'index.html', {})

    return render(request,'login.html',context)

def buy_info(request):
    context = {'form': BuyInfoCrispy()}
    if request.method == 'POST':
        info = BuyInfoModel()
        name = request.POST.get('name')
        email = request.POST.get('email')
        lastname = request.POST.get('lastname')
        address = request.POST.get('address')
        description = request.POST.get('description')
        phone_number = request.POST.get('phone_number')

        info.name = name
        info.email = email
        info.lastname = lastname
        info.address = address
        info.description = description
        info.phone_number = phone_number
        info.save()
    return render(request,'buy-info.html',context)

