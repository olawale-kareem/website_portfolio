from django.db import models

class About(models.Model):
    text = models.CharField(max_length=1000)  
    def __str__(self):
        return self.text

class Dev(models.Model):
    name = models.CharField(max_length=200, default='')
    profile = models.CharField(max_length=200, default='')  
    email = models.EmailField(max_length=200, default='') 
    phone = models.CharField(max_length=20, default='')
    address = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name

   