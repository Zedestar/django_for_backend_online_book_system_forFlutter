from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def exampleFuction(request):
    return JsonResponse(
        {
            "name":"Melkizedeki",
            "age":28
        }
    )
