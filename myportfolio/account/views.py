from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']
        print(user_name)
        # USER = User.objects.get(password=password)
        # print(USER)
        user = auth.authenticate(username=user_name,password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
             return render(request,'account/login.html',{'error':'User name or password is incorrect!'})
    else:
        return render(request,'account/login.html')

def singup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'account/singup.html',{'error':'User name is already been taken'})
            except:
                user = User.objects.create_user(request.POST['username'],request.POST['password1'])
                auth.login(request,user)
                return redirect('home')

        else:
            return render(request,'account/singup.html',{'error':'password must be same'})

    else:
        return render(request,'account/singup.html')

def logout(request):
    if request.method =='POST':

        auth.logout(request)
        return redirect('home')

