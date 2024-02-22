from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.serializers import *



from main.models import Xodimlar,Davomat

@api_view(['GET'])
def employee_list(request):
    employees=Xodimlar.objects.all()
    employees=XodimlarSerializer(employees, many=True)
    return Response(employees.data)


@api_view(['POST'])
def employee_create(request):
    l_name=request.data.get('l_name')
    f_name=request.data.get('l_name')
    if l_name or f_name:
        employees= Xodimlar.objects.create(
            'l_name':l_name,
            'f_name':f_name
        

        )
        employees=XodimlarSerializer(employees, many=True)
        return Response(employees.data)
    

def attendance_add(request):
    data=request.data.get('data')
    davomat=Davomat.objects.create(
        'data':data
    )
    


    



    






    


