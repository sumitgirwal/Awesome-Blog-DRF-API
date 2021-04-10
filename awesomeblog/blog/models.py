from django.db import models

class Post(models.Model):
	title = models.CharField(max_length = 200, null = True)
	description = models.CharField(max_length = 200, null = True)
	created_date = models.DateTimeField(auto_now = True, null = True)

	def __str___(self):
		return self.title +'--'+ self.description


