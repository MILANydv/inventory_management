from django.shortcuts import render
from rest_framework import permissions, viewsets

from .models import Category, Customer, Order, Product, Supplier
from .serializers import (CategorySerializer, CustomerSerializer,
                          OrderSerializer, ProductSerializer,
                          SupplierSerializer)

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ['name', 'description']
    filterset_fields = ['name']

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ['name', 'contact_email', 'phone', 'address']
    filterset_fields = ['name', 'contact_email']

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ['name', 'email', 'phone', 'address']
    filterset_fields = ['name', 'email']

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ['name', 'description']
    filterset_fields = ['name', 'category', 'supplier']

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ['order_type']
    filterset_fields = ['order_type', 'customer', 'supplier']
