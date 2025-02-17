from django.shortcuts import render
from django.http import JsonResponse
from  djanog.contrib.auth.models import User

# Create your views here.


def exampleFuction(request):
    user = User.objects.get(pk=1)
    return JsonResponse(
        {
            "name":"Melkizedeki",
            "age":28
        }
    )
