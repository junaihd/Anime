from django.shortcuts import render,redirect
from django.contrib import messages
from .models import user,source,animemovie
from django.http import JsonResponse
# Create your views here.
def homepage(request):
    return render(request,"home.html")

def loginpage(request):
    if request.method=='POST':
        try:
            userdetails=user.objects.get(emailid=request.POST['E-mail'],password=request.POST['Password'])
            print("E-mail",userdetails)
            request.session['emailid']=userdetails.emailid
            return render(request,'indexx.html')
        except user.DoesNotExist as e:
            messages.success(request,'Email/passwword Invalid..!')    
    return render(request,"login.html")    

def registerpage(request):
    if request.method=='POST':
        Name=request.POST['Name']
        Number=request.POST['Number']
        Email=request.POST['E-mail']
        Password=request.POST['Password']
        user(name=Name,number=Number,emailid=Email,password=Password).save()
        return redirect('loginpage')
        messages.success(request,'The Account '+request.POST['Name']+"is Registed successfully...!")
    return render(request,"register.html")   


def indexpage(request):
    return render(request,"indexx.html")    

def animepage(request):
    movie = source.objects.all()    
    data = {
        'movie': movie
    }
    return render(request,"anime.html",data)    

def contactpage(request):
    return render(request,"contact.html")    

def aboutpage(request):
    return render(request,"about.html")    

def moviepage(request):
    film = animemovie.objects.all()
    data = {
        'film': film
    }
    return render(request,"movie.html",data)

def movieapi(request):
    data=animemovie.objects.values()
    if data:
        return JsonResponse({
            'error':False,
            'message':'movie retrieved successfully',
            'amar':list(data)

        })    
    else:
        return JsonResponse({
            'error':True,
            'message':'movie not retrieved'
        })    

def filmapi(request):
    data=source.objects.values()
    if data:
        return JsonResponse({
            'error':False,
            'message':'film retrieved',
            'don':list(data)
        })
    else:
        return JsonResponse({
            'error':True,
            'message':'film not retrieved'
        })    