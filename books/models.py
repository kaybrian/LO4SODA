from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=50, null=False,unique=True, blank=False)
    author = models.CharField(max_length=100, null=False, blank=False)
    pub_date = models.DateField(null=False,blank=False)
    price = models.FloatField(null=False, blank=False)
    description = models.TextField()\
        
        
    def __str__(self):
        return self.name