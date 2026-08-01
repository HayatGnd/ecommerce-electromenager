from django.db import models

# Create your models here.

class Category(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom 
class Product(models.Model):
    nom = models.CharField(max_length=100)  
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)  
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/' , blank=True , null=True)
    categorie = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nom

