from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def profile(request):
    return JsonResponse(
        {
            "name": "Zedexy your successfull registered, and this is your profile"
        }
    )