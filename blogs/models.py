from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
	text = models.TextField()
	title = models.CharField(max_length=200, unique=True)
	created_at = models.DateTimeField(auto_now=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-id']
