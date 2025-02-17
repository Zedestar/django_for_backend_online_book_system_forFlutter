from django.urls import path, include
from . import views


urlpatterns = [
    
    path("profile", views.profile, name=""),
    path('', include('dj_rest_auth.urls')),
    # Therefore after successful verification then we are taken to this path 
    # accoutns/login and since we have already set the path of account, and which directs us this place, the automatically we can sucess 
    
]
