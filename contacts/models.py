from django.db import models
from datetime import datetime

class Contact(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)
	subject = models.CharField(max_length=200)
	message = models.TextField(blank=True)
	created_at = models.DateTimeField(default=datetime.now, blank=True)
	def __str__(self):
		return self.name

