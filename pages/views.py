from django.shortcuts import render, HttpResponse

# Create your views here.
def home_view(reqvest):

    return render(reqvest, "home.html")

def contact_view(reqvest):
    return render(reqvest, "contact.html")

def about_view(reqvest):
    return render(reqvest, "about.html")

def gallery_view(reqvest):
    return render(reqvest, "gallery.html")
