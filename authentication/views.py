from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django_project import settings
from django.core.mail import send_mail



# Create your views here.
def home(request):
    return render(request,'authentication/home.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'students/index.html', {'fname': fname})
        else:
            messages.error(request, 'The credentials did not match')
            return redirect('home')

    return render(request, 'authentication/signin.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if User.objects.filter(username=username):
            messages.error(request, 'user name already exists, please try another user name!')
            return redirect(home)

        if User.objects.filter(email=email):
            messages.error(request, 'Email already registered, please Sign In instead!')
            return redirect(home)
        
        if len(username)>10:
            messages.error(request, 'username cannot exceed 10 characters!' )

        if pass1 != pass2:
            messages.error(request,'Both passwords do not match! Try again')

        if not username.isalnum():
            messages.error(request,'Username must contain alphabets and numbers only!')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        messages.success(request, 'Your account was created successfully!')

        #welcome email

        subject = 'Welcome to Portal- Django Login!'
        message= "hello " + myuser.first_name + " ! \n\n" +'Welcome to the Portal made by Django- Framework. please Confirm your Email address and lets get Started \n \n Regards \n Saakshi Gajjar \nTeam Django @ HB'
        from_email = settings.EMAIL_HOST_USER
        to_list= [myuser.email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)


    

        return redirect('signin')

    return render(request, 'authentication/signup.html')

def signout(request):
    logout(request)
    messages.success(request,'logged out successfully!')
    return redirect('home')

