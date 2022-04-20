import email
from django.shortcuts import render,HttpResponseRedirect
from requests import request

from enroll.models import User
from .forms import StudentReg

# Create your views here.

# insert and display data :-
def add_show(request):
      if request.method == 'POST':
            fm = StudentReg(request.POST)
            # if fm.is_valid():                # 1st method
            #  fm.save()

            if fm.is_valid():                  # 2nd method
              nm = fm.cleaned_data['name']
              em = fm.cleaned_data['email']
              pw = fm.cleaned_data['password']
              reg = User(name=nm,email=em,password=pw)
              fm.save()        
              fm=StudentReg()


      else:
            fm=StudentReg()
      stud =User.objects.all()
      return render(request,'enroll/add_show.html',{'form':fm,'stu':stud})


# delete :-
def dele(request,id):
 if request.method == "POST":
       pi=User.objects.get(pk=id)
       pi.delete() 
       return HttpResponseRedirect('/')


# update :-

def update_data(request,id):
  if request.method =="POST":
    pi=User.objects.get(pk=id)
    fm=StudentReg(request.POST,instance=pi)
    if fm.is_valid():
      fm.save()
  else :
      pi=User.objects.get(pk=id)
      fm=StudentReg(instance=pi)
  return render(request,'enroll/updates_stud.html',{'form':fm})