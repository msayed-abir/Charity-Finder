from django.shortcuts import render

# Create your views here.

def listofcharityorganizations(request):
    return render(request,'list-of-charity-organizations.html')