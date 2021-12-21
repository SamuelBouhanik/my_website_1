from django.shortcuts import render

def Display_homepage(request):
    return render(request ,'../templates/pages/index.html')
# Create your views here.

def Display_info(request):
    return render(request, '../templates/nous_contacte/info.html')
