from django.db import models
from django.contrib.auth.models import User

# Create your models here.    
class Cordinate(models.Model):
    class Meta:
        db_table = 'Cordinate'
        managed = True
        verbose_name = 'Cordinate'
        verbose_name_plural = 'Cordinates' 
    
    cordinates = models.TextField()
    output = models.TextField()
    distance = models.DecimalField(max_digits=22,decimal_places=20)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User,on_delete=models.PROTECT, related_name="+")
    modified_by = models.ForeignKey(User,on_delete=models.PROTECT, related_name="+")