from django.http import HttpResponse
from django.shortcuts import render

#Maintenance/404 Routes
def maintenance(request):
    return render(request, 'hale_web/under-maintenance.html')



