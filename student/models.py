from django.db import models

# Create your models here.
from email.mime import image
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Student_detail(models.Model):
	name = models.CharField(max_length=200, null=True)
	roll_number = models.CharField(max_length=200, null=True)
	upload = models.ImageField(upload_to ='image')
	
	def __str__(self):
		return self.roll_number
		
class Mark(models.Model):
	
	subject = models.CharField(max_length=200, null=True)