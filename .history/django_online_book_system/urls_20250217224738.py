"""
URL configuration for django_online_book_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls')),    # This is the first line that wants user to be registered
    path('account/', include('allauth.urls'))
]




# So at the first step is to do the registratrion which is provided with registrration path that takes us to dj_rest.auth.registration.urls, this 
# signup the user, on top of that i watn to verify the user using the email that they have user in registration, there for we had to new
# App password in the google account, There for we have to add the configuration to allow message are sent to out google 
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# 
# 
# there fore after successful verification the the 