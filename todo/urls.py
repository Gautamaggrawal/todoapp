"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include,re_path
from rest_auth.registration.views import VerifyEmailView, RegisterView
from django.views.generic import TemplateView
from django.conf.urls import url
from allauth.account.views import ConfirmEmailView




# urlpatterns = [
# 	path('chat/', include('chat.urls')),
#     path('admin/', admin.site.urls),
# ]
from rest_auth.registration.views import VerifyEmailView


# urlpatterns = [
# path('', include('rest_auth.urls')),
# path('login/', LoginView.as_view(), name='account_login'),
# path('registration/', include('rest_auth.registration.urls')),
# path('registration/', RegisterView.as_view(), name='account_signup'),


# ]

from tasks import urls


urlpatterns = [
	path('',include(urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^registration/account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),
    
    
    
    # url(r'', include('rest_auth.urls')),
    # url(r'^registration/', include('rest_auth.registration.urls'))





]