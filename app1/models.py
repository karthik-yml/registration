from django.db import models

# Create your models here.
class EMP(models.Model):
	# id = models.BigAutoField(primary_key=True,default='')
	firstname = models.CharField(max_length = 300,default='')
	lastname = models.CharField(max_length = 300,default='')
	gender = models.CharField(max_length = 10)
	phone = models.IntegerField()
	password = models.CharField(max_length = 300,default='')
	email = models.CharField(max_length=300,default='')
	
    