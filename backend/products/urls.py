from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet


router = DefaultRouter() #outil de Rest framwork qui genere toute les urls automatic

router.register('products', ProductViewSet) #on dit au router genere toutes les urls pour products

'''GET    /api/products/      → liste tous les produits
POST   /api/products/      → crée un produit
GET    /api/products/1/    → détails du produit 1
PUT    /api/products/1/    → modifie le produit 1
DELETE /api/products/1/    → supprime le produit 1'''
router.register('categories', CategoryViewSet)

urlpatterns = [
    path('',include(router.urls)),
]