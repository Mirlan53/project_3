from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	photo = models.ImageField(upload_to='users_photos', null=True, blank=True)
	birth_date = models.DateField()
	bio = models.TextField()
	education = models.CharField(max_length=150)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	grade = models.IntegerField()


	def __str__(self):
		return self.user.username
