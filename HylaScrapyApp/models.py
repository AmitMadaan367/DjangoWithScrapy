from django.db import models

# Create your models here.
class ProgramUrls(models.Model):
    program = models.CharField(max_length=200, default="", null=True,blank=True,)
    url = models.CharField(max_length=200, default="", null=True,blank=True,)
    def __str__(self):
    	return str(self.program)