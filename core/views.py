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




