from django.urls import path
from . import views
urlpatterns=[
	path('home',views.home,name='home'),
	path('login',views.login_view,name='login view'),
	path('register',views.register_view,name='register view'),
	]