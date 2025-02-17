from django.urls import path
from . import views
from  djanog.aut

urlpatterns = [
    path('first/', views.exampleFuction, name="core"),
]
