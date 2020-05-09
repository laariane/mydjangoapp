from django.shortcuts import render
from django.template import loader
from .models import Etudiant , Module , Note
from django import template


# Create your views here.
from django.http import HttpResponse
def index(request):
	etudiant_list = Etudiant.objects.order_by('-nom')
	moyenne_list=Etudiant.moyenne(etudiant_list)	
		
	

	

	
	context= {
		'etudiant_list':etudiant_list,
		'moyenne_list':moyenne_list,
		'range':range(len(etudiant_list)) }
	return render(request,'administrateur/index.html',context)


def etudiant_details(request , etudiant_id):
	etudiant_details=Etudiant.objects.get(pk=etudiant_id)
	context = {etudiant_details :'etudiant_detials'}
	return render(request, 'administrateur/etudiant_details',context)
