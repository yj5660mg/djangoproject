from django.db import models

class Movie(models.Model):
	MOVitem = models.CharField(max_length=200)
	watched = models.BooleanField(default=False)


	def __str__(self):
		return self.MOVitem + ' | ' + str(self.watched)