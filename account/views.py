from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request):
    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2: #Checking two password if they are same
            if User.objects.filter(username=username).exists(): #Checking the username, if it is already exists in the database
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists(): #Checking the email, if it is already exists in the database
                messages.info(request,'Email Taken')
                return redirect('register')   
            else:

                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print("User Created")
        else:
            messages.info(request,'Password not matching')
            return redirect('register')    
        return redirect('/')

    else:

        return render(request,'register.html')