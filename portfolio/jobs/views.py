from django.shortcuts import render

def index(request):
    return  render(request,'jobs/home.html')
