"""trp_assistant_bot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include 
from django.contrib import admin
from trp_assistant_bot.settings import URL_API_PREFIX
from rest_framework.authtoken.views import obtain_auth_token
from open_course.views import TokenValidate

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('view_loader.urls')),
    url(URL_API_PREFIX+r'courses/', include('open_course.urls')),
    url(URL_API_PREFIX+r'database_loader/', include('database_loader.urls')),
	url(URL_API_PREFIX+r'template_editor/', include('template_editor.urls')),
	url(URL_API_PREFIX+r'auth-token/', obtain_auth_token),
	url(URL_API_PREFIX+r'token/$', TokenValidate.as_view()),    
	url(r'^', include('mail_sender.urls'))
]
