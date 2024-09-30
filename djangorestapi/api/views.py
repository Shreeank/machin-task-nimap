from django.shortcuts import render, HttpResponse

# Create your views here.
from .models import client, Project
from .serializers import clientserializer, ProjectSerializer ,UserLoginSerializer
from rest_framework.renderers import JSONRenderer

import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist

from .models import User
from .serializers import UserSerializer

# Create your views here.
class UserRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Registered Successfully'},status=status.HTTP_200_OK)
        return Response({'serializer.errors': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UserLoginView(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = User.objects.all().filter(email=email, password=password)
            print("user=",user)
            if user:
                return Response({'msg': 'Login Successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': {'non_field_errors':['Email or Password is not valid']}}, status=status.HTTP_404_NOT_FOUND)



def home(request):
    return render(request,"home.html")


def clientdetails(request,email,password):
    s = client.objects.get(id=id)
    serializer = clientserializer(s)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type="application/json")

def clientdetails(request,id):
    s = client.objects.get(id=id)
    serializer = clientserializer(s)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type="application/json")

def client_list(request):
    cl=client.objects.all()
    serializer = clientserializer(cl, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type="application/json")

def projectdetails(request,id):
    p = Project.objects.get(id=id)
    serializer = ProjectSerializer(p)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type="application/json")
#
#
@csrf_exempt
def client_create(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = clientserializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data inserted'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def project_create(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = ProjectSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data inserted'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

def project_details(request):
    p = Project.objects.all()
    serializer = ProjectSerializer(p,many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type="application/json")

def deleteclient(request,id):
    data = client.objects.get(id=id)
    data.delete()
    res={'msg':'record deleted successfully'}
    json_data = JSONRenderer().render(res)
    return HttpResponse(json_data,content_type='application/json')

def deleteProject(request,id):
    data = Project.objects.get(id=id)
    data.delete()
    res={'msg':'record deleted successfully'}
    json_data = JSONRenderer().render(res)
    return HttpResponse(json_data,content_type='application/json')

# def upadateclient(request,id):
#     data = client.objects.get(id=id)
#     data = clientserializer(instance=client, data=request.data)
#     # data.upadate()
#     res = {'msg':'record update successfully'}
#     json_data = JSONRenderer().render(res)
#     if data.is_valid():
#         data.save()
#     return HttpResponse(json_data, content_type='application/json')


@api_view(['POST'])
def updateclient(request, id):
    item = client.objects.get(id=id)
    data = clientserializer(instance=item, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)