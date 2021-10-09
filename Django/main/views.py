from django.shortcuts import render

#from django.http import HttpResponse

# Create your views here.

def main(request):
    context = {
        "title": "Home"    
    }
    return render(request, "home/home.html", context)

