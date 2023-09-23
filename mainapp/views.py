from django.shortcuts import render,redirect
from .forms import RegisterForm,Addfile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from .models import*

# Create your views here.
def home(r):
    
    return render(r,'home.html')

def register(r):
    form=RegisterForm(r.POST or None)
    if (r.method=="POST"):
        if form.is_valid():
           
            return redirect(home)
    return render(r,'register.html',{'form':form})

def loginfun(r):
    form=AuthenticationForm(r.POST or None)
    username=r.POST.get('username')
    password=r.POST.get('password')
    user=authenticate(username=username,password=password)
    if user is not None:
        login(r,user)
        return redirect(home)
    return render(r,'login.html',{'form':form})

def addfile(r):
    form=Addfile(r.POST or None,r.FILES or None)
    if(r.method=='POST'):
        if form.is_valid():
            a = form.save(commit=False)
            a.usern = r.user
            a.save()
            
            return redirect(home)
    return render(r,'addfile.html',{'form':form})

def user_file(r):
    curnt_user=r.user
    files=File.objects.filter(usern=curnt_user)
    return render(r,'files.html',{'files':files})




def delete_file(request,id):
    file=File.objects.get(id=id)
    file.delete()
    return redirect(user_file)


def logoutfun(r):
    logout(r)
    return redirect(loginfun)
