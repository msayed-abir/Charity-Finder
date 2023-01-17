from django.shortcuts import render,redirect
from charityorganization.form import charityForm
from charityorganization.models import Charityorg


# Create your views here.

def create(request):

    if request.method == "POST":
        form = charityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/all-charityorganization")
    else:
        form = charityForm()

    return render(request,'create.html',{'form':form})

def show(request):
    showorg = Charityorg.objects.all()
    return render(request,"show.html",{'showorg':showorg})

def delete(request,id):
    charity = Charityorg.objects.get(id=id)
    charity.delete()
    return redirect("/all-charityorganization")

def edit(request,id):
    charity = Charityorg.objects.get(id=id)
    return render(request,"edit.html",{"charityorganization":charity})

def update(request,id):
    charity = Charityorg.objects.get(id=id)
    form = charityForm(request.POST,instance=charity)

    if form.is_valid():
        form.save()
        return redirect("/all-charityorganization")

    return render(request,"edit.html",{"charityorganization":charity})