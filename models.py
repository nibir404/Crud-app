from django.db import models

# Create your models here.
class Insert(models.Model):
    name = models.CharField(max_length=100)
    f_name = models.CharField(max_length=100)
    m_name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
