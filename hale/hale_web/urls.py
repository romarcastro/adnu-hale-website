from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage,  name=""),
    path('user-logout', views.user_logout, name="user-logout"),

   
    #health staff routes 
    path('staff-login', views.hstafflogin, name="staff-login"),
    path('staff-register', views.hstaffregister, name="staff-register"),
    path('staff-index', views.hstaffindex, name="staff-index"),
    path('staff-appointments', views.staffAppointments, name="staff-appointments"),

    path('appointment-details', views.appointmentDetails, name="appointment-details"),

    #normal user routes 
    path('user-login', views.userlogin, name="user-login"),
    path('user-register', views.userregister, name="user-register"),
    path('user-index', views.userindex, name="user-index"),

    #test routes - dont mind
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('dashboard', views.dashboard, name="dashboard"),
    

    path('accept/', views.accept, name='accept_page'),
]