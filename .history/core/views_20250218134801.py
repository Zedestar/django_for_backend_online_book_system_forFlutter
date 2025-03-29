from django.shortcuts import render
from django.http import JsonResponse
from  django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def exampleFuction(request):
   nameFromFlutter = request.POST['name']
   ageFromFlutter = request.POST['age']
   print(f"these are data from Flutter: {nameFromFlutter} and {ageFromFlutter} respectively.  I am a Django view.  I am returning the same data back to Flutter.  Thank you!  :)  ")
   return JsonResponse(
        {
            "name":nameFromFlutter,
            "age": ageFromFlutter,
        }
    )




# Customized login view 
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class CustomLoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(request, email=email, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
