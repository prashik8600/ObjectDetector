from django.db import models

class img(models.Model):
    photo=models.ImageField(upload_to='allimg')
    date=models.TimeField(auto_now_add=True)
    files=models.FileField(upload_to='documents')
    
