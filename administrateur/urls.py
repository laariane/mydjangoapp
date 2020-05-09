from django.urls import path
from . import views
urlpatterns=[
	path('',views.index,name='index'),
	path('etudiant_details',views.etudiant_details, name='etudiant details'),
]