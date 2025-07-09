from django.contrib import admin

from .models import Category, Customer, Order, OrderItem, Product, Supplier


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name', 'description')
    list_filter = ('name',)

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact_email', 'phone', 'address')
    search_fields = ('name', 'contact_email', 'phone', 'address')
    list_filter = ('name',)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'address')
    search_fields = ('name', 'email', 'phone', 'address')
    list_filter = ('name', 'email')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'supplier', 'price', 'stock')
    search_fields = ('name', 'description')
    list_filter = ('category', 'supplier')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_type', 'customer', 'total', 'date')
    search_fields = ('order_type',)
    list_filter = ('order_type', 'customer')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'price')
    search_fields = ('order__id', 'product__name')
    list_filter = ('order', 'product')
