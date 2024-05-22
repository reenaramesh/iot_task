from django.shortcuts import render

# Create your views here.


from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.response import Response 
from .models import Device

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from .serializers import DeviceSerializer
from rest_framework.decorators import api_view
from rest_framework import status
 
from rest_framework.decorators import api_view


@api_view(['GET','POST'])
def device_list(request):
    device = Device.objects.all()
        
    if request.method == 'GET': 
        device_serializer = DeviceSerializer(device, many=True)
        return JsonResponse(device_serializer.data, safe=False)

    elif request.method == 'POST':
        device = JSONParser().parse(request)
        device_serializer = DeviceSerializer(data=device)
        if device_serializer.is_valid():
            device_serializer.save()
            return JsonResponse(device_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(device_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    


@api_view(['GET', 'PUT', 'DELETE'])
def device_detail(request, device_id):
    try: 
        device = Device.objects.get(device_id=device_id) 
        #return JsonResponse(device) 
    except Device.DoesNotExist: 
        return JsonResponse({'message': 'The device does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        device_serializer = DeviceSerializer(device) 
        return JsonResponse(device_serializer.data) 
    
 
    
    elif request.method == 'PUT': 
        device_data = JSONParser().parse(request) 
        device_serializer = DeviceSerializer(device, data=device_data) 
        if device_serializer.is_valid(): 
            device_serializer.save() 
            return JsonResponse(DeviceSerializer.data,safe=True) 
        return JsonResponse("Successfully updated") 
 


    elif request.method == 'DELETE': 
        device = Device.objects.get(device_id=device_id)
        device.delete() 
        #return JsonResponse(device)
        return JsonResponse({'message': 'device was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    