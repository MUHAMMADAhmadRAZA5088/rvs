from cmath import pi
from django.forms import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import User
from .form import StudentResistration

# Create your views here.
# this is show new function and all function


def add_show(request):
    if request.method=='POST':
        ft=StudentResistration(request.POST)
        if ft.is_valid():
            nm=ft.cleaned_data['Name']
            em=ft.cleaned_data['Email']
            ps=ft.cleaned_data['password']
            reg=User(Name=nm,Email=em,password=ps)
            reg.save()
            ft=StudentResistration()

    else:
        ft=StudentResistration()
    st=User.objects.all()
    return render(request,'addandshow.html',{'form':ft,'stud':st})

#this will delete function
def dele(request,id ):
    if request.method=='POST':
         kl=User.objects.get(pk=id)
         kl.delete()
         return HttpResponseRedirect('/')
# this function update and edit
def add_update(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=StudentResistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=StudentResistration(instance=pi)
    return render(request,'update.html',{'form':fm})
        

    

