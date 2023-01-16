from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import Group
from uaa.models import Profile,User
from django.contrib.auth import authenticate,login,logout
import uuid

from django.conf import settings
from django.core.mail import EmailMessage
from django.core.mail import send_mail

# Create your views here.
def LoginView(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('Email')
            password = request.POST.get('Password')
            
            user_instance = User.objects.filter(email=username).first()
            if user_instance is None:
                messages.info(request,'User not found')
                return redirect('login_url')
            
            profile_instance = Profile.objects.filter(user=user_instance).first()
            if not profile_instance.is_verified:
                messages.info(request, 'User not verified')
                return redirect('login_url')
            
            user = authenticate(request, email=username, password=password)
            if user is not None and user.is_active:
                login(request,user)
                # messages.success(request, 'Your are now logged in !!')
                
                return redirect('dashboard_url')
    
            else:
                messages.warning(request, 'Invalid Credentials !!')
                return redirect('login_url')
                
    except Exception as e:
        raise e
    
    context = {}
    return render(request,"login.html")

def RegisterView(request):
    
    try:
        if request.method == 'POST':
            username = request.POST.get('Username')
            email = request.POST.get('Email')
            password = request.POST.get('Password')
            password1 = request.POST.get('ConfirmPassword')
            
            if User.objects.filter(username=username).first():
                messages.info(request,'Username is already taken')
                return redirect('register_url')
            
            if User.objects.filter(email=email).first():
                messages.info(request,'Email is already taken')
                return redirect('register_url')
            
            if len(username) < 5:
                messages.info(request,'username, atlest 5 characters')
                return redirect('register_url')
            
            if password != password1:
                messages.info(request,'password does not match')
                return redirect('register_url')
            
            if len(password) < 8:
                messages.info(request, 'password, 8 mixed characters required')
                return redirect('register_url')
            
            #Creating and saving a user to the database.
            user_obj = User(username=username, email=email)
            user_obj.set_password(password)
            user_obj.save()
            
            #Adding a default role to the registered user.
            grp = Group.objects.get(name="technician")
            user= User.objects.get(username=username)
            user.groups.add(grp)
            
            #creating a user profile.
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user=user_obj, auth_token=auth_token)
            profile_obj.save()
            
            #Sending email for verification.
            try:
                SendEmailRegister(email, auth_token)
            except Exception as e:
                return HttpResponse(e)
            
            messages.info(request,'Check your email to verify.')
            return redirect('login_url')
        
    except Exception as e:
        return HttpResponse(e)
    
    context = {}
    return render(request,"uaa/register.html")

#A function for sending email for verification.
def SendEmailRegister(email, token):
    subject = 'Your accounts needs to be verified'
    message = f'Hi verify your account 127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message,email_from,recipient_list)


#Verify your account.
def VerifyView(request, auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request,'Your account is alredy verified')
                return redirect('login_url')
             
            profile_obj.is_verified = True
            profile_obj.save() 
            messages.success(request,'Your account has been verified')
            return redirect('success_url')
        
        else: 
            return redirect('error_url')
    except Exception as e:
        return HttpResponse(e)


def ResetPasswordView(request):
     
    try:
        if request.method == 'POST':
            email = request.POST.get('Email')
            
            user_email_instance = User.objects.filter(email=email).first()
            if user_email_instance is None:
                messages.info(request,'Email does not exist.')
                return redirect('resetpassword_url')
            
            try:
                SendEmailPasswordResetView(email)
            except Exception as e:
                return HttpResponse(e)
            
            messages.info(request,'Check your email, change password.')
            return redirect('login_url')
        
    except Exception as e:
        raise e
    
    context = {}
    return render(request,"uaa/resetpassword.html")

def SendEmailPasswordResetView(email):
    subject = 'password reset, click the link below'
    message = f'Hi verify your account 127.0.0.1:8000/RecoverPassword/{email}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message,email_from,recipient_list)


def RecoverPasswordView(request, email):
    
    try:
        if request.method == 'POST':
            password = request.POST.get('Password')
            confirmPassword = request.POST.get('ConfirmPassword')
            passwordLength = len(password)
            
            userEmailInstance = User.objects.filter(email=email).first()
            if userEmailInstance:
                if password != confirmPassword:
                    messages.info(request, 'password does not match')
                    return redirect('resetpassword_url')
            
                if passwordLength < 8:
                    messages.info(request, 'password is too short')
                    return redirect('resetpassword_url')
                
                userEmailInstance.set_password(password)
                userEmailInstance.save()
                messages.info(request,'password set')
                return redirect('login_url')
            
    except Exception as e:
        return HttpResponse(e)
    
    context = {}
    return render(request,"uaa/recoverPassword.html")


def DashboardView(request):
    
    context = {}
    return render(request,"uaa/dashboard.html")


def ProfileView(request):
    
    context = {}
    return render(request,"uaa/profile.html")


def SuccessView(request):
    
    context = {}
    return render(request,"uaa/success.html")


def TokenSendView(request):
    
    context = {}
    return render(request,"uaa/tokensend.html")


def ErrorView(request):
    
    context = {}
    return render(request,"uaa/error.html")


def UaaUserListView(request):
    roleInstance = Group.objects.all()
    
    context = {'roleInstanceData': roleInstance}
    print(roleInstance)
    return render(request, 'uaa/uaaUserList.html', context)


def CreateUserView(request):
    pass


def LogoutView(request):
    logout(request)
    return redirect('login_url')
