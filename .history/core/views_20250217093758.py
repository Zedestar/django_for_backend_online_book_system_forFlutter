from django.shortcuts import render
from django.http import JsonResponse
from  django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def exampleFuction(request):
    user = User.objects.get(pk=1)
    return JsonResponse(
        {
            "name":user.username,
            "age": user.password,
        }
    )
