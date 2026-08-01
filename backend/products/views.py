from rest_framework import viewsets
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet): #categoryviewset herite tout les methodes de viewset
    queryset = Category.objects.all() #outil qui parle direct a la base de donnee pour recuperer les categories # → SELECT * FROM products_category;
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all() #outil qui parle direct a la base de donnee pour recuperer les produits
    serializer_class = ProductSerializer
