from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import User
from .models import Student

# Create your views here.

def add(request):
    if request.method=='POST':
        obj=User(request.POST)
        if obj.is_valid():
            name1=obj.cleaned_data['name']
            email1=obj.cleaned_data['email']        #or obj.save()
            passw1=obj.cleaned_data['password']
            reg=Student(name=name1,email=email1,password=passw1)
            reg.save()
            obj=User()
    else:
        obj=User()

    stud=Student.objects.all()
    return render(request,'crud/addandshow.html',{'keys':obj,'dict':stud})



#for delete

def delete(request,id):
    if request.method=='POST':
        pi=Student.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/home/add/')


#for update


def update(request,id):
    if request.method=='POST':
        pi=Student.objects.get(pk=id)
        fm=User(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/home/add/')
    else:
        pi=Student.objects.get(pk=id)
        fm=User(instance=pi)
    return render(request,'crud/updatestudent.html',{'foom':fm})