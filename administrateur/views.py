from django.shortcuts import render
from django.template import loader
from .models import Etudiant,Module,Note

# Create your views here.
from django.http import HttpResponse
def index(request):
	etudiant_list = Etudiant.objects.order_by('-nom')
	print(etudiant_list)
	context= {'etudiant_list':etudiant_list, }
	return render(request,'administrateur/index.html',context)
