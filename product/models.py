from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(req):
        return render, name()
