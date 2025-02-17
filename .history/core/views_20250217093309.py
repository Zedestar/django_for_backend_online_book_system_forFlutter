from django.shortcuts import render
from django.http import JsonResponse
from  django.contrib.auth.models import User

# Create your views here.


def exampleFuction(request):
    user = User.objects.get(pk=1)
    return JsonResponse(
        {
            "name":user.usename,
            "age": user.password,
        }
    )
