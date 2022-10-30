from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as LoginUser
from django.contrib.auth.models import User
from django.contrib import messages
from .models import LocalUsers
# Create your views here.

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('/')
    # Redirect to a success page.



def index(request):
    return render(request,'index3.html')

def register(request):
    content = { 'ErrorMessage':None,'UserName':False,'IsBanned':False }
    if request.method=='POST':
        UserName  =  request.POST['UserName']
        Password  =  request.POST['Password']
        FirstName =  request.POST['FirstName']
        LastName  =  request.POST['LastName']
        Email     =  request.POST['Email']

        if User.objects.filter(username=UserName).exists():
            content['ErrorMessage'] = 'This username is already taken'
            return render(request,'forme.html',{'data':content})
        else:
            user = User(username=UserName,first_name=FirstName,last_name=LastName,email=Email)
            user.set_password(Password)
            user.save()
            if user is not None:
              LoginUser(request, user)
              print('loged in')

        return redirect('/')
    else:
        return render(request,'forme.html',{'data':content})


def login(request):
    if request.method=='POST':
        UserName = request.POST['UserName']
        Password = request.POST['Password']
        user = authenticate(username=UserName,password=Password)
        print(user)
        print(UserName)
        print(Password)
        if user is not None:
            LoginUser(request, user)
            return redirect('/')
        else:
            ErrorMessage = 'Username / Password is incorrect'
            return render(request,'logins.html',{'ErrorMessage': ErrorMessage})
    else:
        return render(request,'logins.html')

