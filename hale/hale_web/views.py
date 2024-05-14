from django.shortcuts import render, redirect
from . forms import LoginForm, CustomUserCreationForm

# Authentication models and functions
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

# Protect Views
from django.contrib.auth.decorators import login_required

#For Javascript redirect
from django.http import JsonResponse
from django.urls import reverse

#Health Staff Routes
def hstafflogin(request):
    form = LoginForm()
    if request.method == "POST": 
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("staff-index")

    context = {'loginform': form}            
    return render(request, 'hale_web/sign-in-health-staff.html', context=context)

def hstaffregister(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
        
    return render(request, 'hale_web/sign-up-health-staff.html', {'registerform': form})
#healthstaff dashboard
@login_required(login_url="staff-login")
def hstaffindex(request):
    return render(request, 'hale_web/health-staff-index.html')

@login_required(login_url="staff-login")
def staffAppointments(request):
    return render(request, 'hale_web/health-staff-appointments.html')

@login_required(login_url="staff-login")
def appointmentDetails(request):
    return render(request, 'hale_web/appointment-details.html')

# User Routes
def userlogin(request):
    form = LoginForm()
    if request.method == "POST": 
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("user-index")

    context = {'loginform': form}            
    return render(request, 'hale_web/sign-in-user.html', context=context)


def userregister(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
        
    return render(request, 'hale_web/sign-up-user.html', {'registerform': form})

@login_required(login_url="user-login")
#user dashboard
def userindex(request):
    return render(request, 'hale_web/user-templates/user-landing-page.html')

@login_required(login_url="user-login")
def userAppointmentBooking(request):
    return render(request, 'hale_web/user-templates/user-appointment-page.html')

@login_required(login_url="user-login")
def userConfirmAppointment(request):
    return render(request, 'hale_web/user-templates/user-confirmation-page.html')



def user_logout(request):
     auth.logout(request)
     return redirect("")


# Test Routes

def maintenance(request):
    return render(request, '404.html')

def homepage(request):
     return render(request, 'hale_web/splash.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'hale_web/sign-up-health-staff.html', {'registerform': form})

def login(request): 
    form = LoginForm()
    if request.method == "POST": 
         
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            #authenticate userr
            user = authenticate(request, username=username, password=password)

            #if user exists
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")

    context = {'loginform': form}            
    return render(request, 'hale_web/sign-in-health-staff.html', context=context)

#Javascript Redirect
def accept(request):
    # Get the URL of the target page
    target_page_url = reverse('staff-appointments')
    
    # Return the target page URL in JSON format
    return JsonResponse({'redirect_url': target_page_url})

@login_required(login_url="staff-login")
#testroutes
def dashboard(request):
        return render(request, 'hale_web/health-staff-index.html')




