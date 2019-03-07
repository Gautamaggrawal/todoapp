from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.null_view, name='password_reset_confirm'),
	url(r'^registration/account-email-verification-sent/', views.null_view, name='account_email_verification_sent'),
	url(r'^registration/complete/$', views.complete_view, name='account_confirm_complete'),
	path('welcome',views.index),
	path('profile/',views.profile),
	path('createtodo/',views.TodoCreateView.as_view()),
	path('viewtodo',views.TodoRetrieveView.as_view()),
	url(r'^todoupdate/(?P<pk>[0-9]+)$', views.TodoUpdateView.as_view()),
	url(r'^tododelete/(?P<pk>[0-9]+)$', views.TodoDeleteView.as_view()),	
	]