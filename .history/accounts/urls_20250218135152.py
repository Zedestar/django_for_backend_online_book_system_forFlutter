from django.urls import path, include
from .views import *


urlpatterns = [
    
    path("profile/", profile, name=""),
    path("login/", CustomLoginView.as_view()),
    # path('', include('dj_rest_auth.urls')),
    # Therefore after successful verification then we are taken to this path 
    # accoutns/login and since we have already set the path of account, and which directs us this place, the automatically we can sucess 
    
]
