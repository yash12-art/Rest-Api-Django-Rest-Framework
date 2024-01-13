from django.shortcuts import render
from rest_framework.decorators import api_view
from Register_App.serializers import Regsiterserializer
from rest_framework import serializers,status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

@api_view(['POST',])
def Registration(request):
    if request.method=='POST':
        serializer=Regsiterserializer(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['response']="Registration Successful"
            data['username']=account.username
            data['email']=account.email
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data=serializer.errors
        return Response(data,status=status.HTTP_201_CREATED)
    
