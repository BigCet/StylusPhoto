from django.shortcuts import render, HttpResponse

# Create your views here.
def home_view(reqvest):
    return HttpResponse("Hello World")

def contact_view(reqvest):
    return HttpResponse("Contakt page")

def about_view(reqvest):
    return HttpResponse("About page")

