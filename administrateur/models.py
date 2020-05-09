from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import statistics

# Create your models here.
class Etudiant(models.Model):
	def __str__(self):
		return self.nom
	etudiant_id = models.IntegerField(primary_key=True)
	nom = models.CharField(max_length=200,null = True)
	prenom = models.CharField(max_length=200,null = True)
	#la logique de la moyenne
	
	
	def moyenne( etudiant_list):
		
		moyenne_list=[]
		
		for etudiant in etudiant_list :
			
			 
			notes = etudiant.note_set.all()
			
			
			l=[]
			
			for note in notes :
				l.append(note.note)
			a=statistics.mean(l)
		 
			moyenne_list.append(a)

		return moyenne_list
		
	
		
class Module(models.Model):
	def __str__(self):
		return self.label
	edtudiant = models.ManyToManyField(	Etudiant)
	
	label = models.CharField(max_length=200,null = True)
	details = models.CharField(max_length=200,null = True)
class Note(models.Model):
	def __str__(self):
		return str(self.note) 
	etudiant = models.ForeignKey(Etudiant , null = True, on_delete=models.CASCADE)
	module = models.ForeignKey(Module , null = True, on_delete=models.SET_NULL)
	note =models.IntegerField(
	default=1,
	validators=[
	    MaxValueValidator(20),
	    MinValueValidator(0)
	]
	)
	
	



