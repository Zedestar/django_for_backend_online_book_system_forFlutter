from django.urls import path
from . import views
from  djanog.contri

urlpatterns = [
    path('first/', views.exampleFuction, name="core"),
]
