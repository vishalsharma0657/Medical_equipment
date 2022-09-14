from django.shortcuts import render
import re
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils.functional import keep_lazy_text
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from medicall.models import User
from medicall.models import Product
from medicall.serializers import UserSerializer

# Create your views here.

@csrf_exempt
def user(request):
    if request.method == 'GET':
        schat = User.objects.all()
        serializer = UserSerializer(schat, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def user1(request , pk):
    try:
        schat = User.objects.get(pk=pk)
       
    except User.DoesNotExist:
        res={'result':'username nottt found'}  
        return JsonResponse(res)

    if request.method == 'GET':
        serializer = UserSerializer(schat)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(schat, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        schat.delete()
        return HttpResponse(status=204)

# adding Users ---------------

@csrf_exempt
def addUser(request):
    data = JSONParser().parse(request)
    myName=data['name']
    myPhone=data['phone_no']
    myemail_id=data['email_id']
    mydp=data['dp']
    mypassword=data['password']
    Myseller=data['seller']
    res={'result':'Email already taken'}   
    try:
        z = User.objects.get(email_id=myemail_id)
        return JsonResponse(res) 
    except User.DoesNotExist:
        try:
            y = User.objects.get(phone_no=myPhone)
            res['result']='phone number already used'
            return JsonResponse(res) 
        except:
            dy={
                "id":myPhone,
                "name":myName,
                "phone_no":myPhone,
                "email_id":myemail_id,
                "dp":mydp,
                "password":mypassword,
                "seller":Myseller,
               }
            srlz=UserSerializer(data=dy)
            if srlz.is_valid():
                srlz.save()
            res['result']='user successfully registered'
        return JsonResponse(res)

# for authentication
@csrf_exempt
def auth(request ):
    data = JSONParser().parse(request)
    passWord=data['password']
    phoneNo=data['phone_no']
    res={'result':'user already exists'}
    try:
        schat = User.objects.get(pk=passWord)
        serializer = UserSerializer(schat)
        d=(dict(serializer.data))
        if d['phone_no']==phoneNo:
            res['result']='old bakra'
            return JsonResponse(res)
        else:
            res['result']=' phone number and password donot match'
            return JsonResponse(res)
    except User.DoesNotExist:
        try:
            schat = User.objects.get(phone_no=phoneNo)
            res['result']='please check your password'
            return JsonResponse(res)

        except User.DoesNotExist:
            res['result']='new bakra'
            return JsonResponse(res)


# Product functions

@csrf_exempt
def user(request):
    if request.method == 'GET':
        schat = User.objects.all()
        serializer = UserSerializer(schat, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)