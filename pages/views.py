from django.http import HttpResponse
from django.shortcuts import render,redirect

from django.contrib.auth.models import User
from django.contrib.auth import logout

from ..text.models import Text
from .forms import *

import re



# HomePage
def composeHome(request):
    return render(request, 'home.html')

def composeText(request):
    idnum = request.GET.get('id')
    obj = Text.objects.get(pk = idnum)
    return render(request,'entry.html',{'entry':obj})


def composeIndex(request):
    items = Text.objects.all()
    return render(request, 'index.html',{'items':items})


# Create an article
def composeEdit(request):
    idnum = request.GET.get('id')
    obj = Text.objects.get(pk = idnum)
    if request.method == 'POST':
        form = EditTextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['originalText']
            text = re.sub(r'\n+','</p><p>',text)
            text = '<p>' + text + '</p>'
            Text.objects.create(text = text)
            return render(request, 'edit.html',{'form':form})
    else:
        form = EditTextForm()
    return render(request, 'edit.html',{'form':form})






# Sign up page
def composeSignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user = User.objects.create_user(username,password,email)
            if first_name:
                user.first_name = first_name
            if last_name:
                user.last_name = last_name
            user.save()
            return redirect('/home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html',{'form':form})

def LogoutRedirect(request):
    logout(request)
    return redirect('/home')

def composeProfile(request):
    return render(request,'profile.html')