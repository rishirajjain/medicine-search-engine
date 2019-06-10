from django.shortcuts import render
from .models import Medicines,BoerickeJoints
# Create your views here.
def home_view(request):
    obj= Medicines.objects.all()
    context={
        'object':obj,
       
    }
    return render(request,"list_meds.html",context)


def med_view(request):
    ob= BoerickeJoints.objects.all()
    context={
        'object':ob,
       
    }
    return render(request,"med.html",context)

#To make simple total matching searches

""" query = request.GET.get('q') 
    
    results = Medicines.objects.filter(medDetails=query)
    context={
        'object':obj,
        'results':results
    } """