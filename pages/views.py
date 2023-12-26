from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth.models import User

from text.models import Text
from .forms import CreateTextForm, SignUpForm





# HomePage
def composeHome(request):
    return render(request, 'navbar.html')

def composeText(request):
    idnum = request.GET.get('id')
    obj = Text.objects.get(pk = idnum)
    text = obj.text
    time = obj.date
    return render(request,'entry.html',{'text':text,'time':time})






# Create an article
def composeCreate(request):
    if request.method == 'POST':
        form = CreateTextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['originalText']
            Text.objects.create(text = text)
            return render(request, 'create.html',{'form':form})
    else:
        form = CreateTextForm()
    return render(request, 'create.html',{'form':form})






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
            return render(request, 'signup.html',{'form':form})
    else:
        form = SignUpForm()
    return render(request, 'signup.html',{'form':form})