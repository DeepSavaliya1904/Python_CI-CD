from django.shortcuts import render

# Create your views here.
def indexPage(req):
    return render(req,'index.html')

def registerPage(req):
    return render(req,'register.html')

def loginPage(req):
    return render(req,'login.html')