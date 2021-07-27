from django.db import models
from django.db.models.base import Model

# Create your models here.




class CordinatesGroup(models.Model):
    class Meta:
        db_table = 'CordinatesGroup'
        managed = True
        verbose_name = 'CordinatesGroup'
        verbose_name_plural = 'CordinatesGroups' 
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(blank=False, null=False, max_length=60)
    modified_by = models.CharField(blank=False, null=False, max_length=60)
    
class Cordinate(models.Model):
    class Meta:
        db_table = 'Cordinate'
        managed = True
        verbose_name = 'Cordinate'
        verbose_name_plural = 'Cordinates' 
    cordinate_group = models.ForeignKey(CordinatesGroup)
    x_cordinate = models.IntegerField()
    y_cordinate = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(blank=False, null=False, max_length=60)
    modified_by = models.CharField(blank=False, null=False, max_length=60)