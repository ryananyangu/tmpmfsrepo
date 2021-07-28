from django.db import models
from django.db.models.base import Model

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
    created_by = models.CharField(blank=False, null=False, max_length=60)
    modified_by = models.CharField(blank=False, null=False, max_length=60)