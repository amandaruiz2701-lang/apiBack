from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def employeeView(request):
    emp =  {
        'id':123,
        'nombre':'Clark',
        'email':'ejemplo@gmail.com',
        'salary':'5000'    
    }
    return JsonResponse(emp)