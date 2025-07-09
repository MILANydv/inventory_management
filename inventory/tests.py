from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from inventory.models import Category, Customer, Order, Product, Supplier

# Create your tests here.

class InventoryAPITestCase(APITestCase):
    def setUp(self):
        # Create user and get JWT token
        self.user = User.objects.create_user(username='apitestuser', password='testpass123')
        url = reverse('login')
        response = self.client.post(url, {'username': 'apitestuser', 'password': 'testpass123'})
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_category_crud(self):
        # Create
        url = reverse('category-list')
        data = {'name': 'Stationery', 'description': 'Office supplies'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        category_id = response.data['id']
        # List
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Retrieve
        url_detail = reverse('category-detail', args=[category_id])
        response = self.client.get(url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Update
        response = self.client.put(url_detail, {'name': 'Updated', 'description': 'Updated desc'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Delete
        response = self.client.delete(url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_supplier_crud(self):
        url = reverse('supplier-list')
        data = {'name': 'Test Supplier', 'contact_email': 'sup@example.com', 'phone': '1234567890', 'address': 'Test Address'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        supplier_id = response.data['id']
        # List
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Retrieve
        url_detail = reverse('supplier-detail', args=[supplier_id])
        response = self.client.get(url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Update
        response = self.client.patch(url_detail, {'phone': '9999999999'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Delete
        response = self.client.delete(url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_customer_crud(self):
        url = reverse('customer-list')
        data = {'name': 'Test Customer', 'email': 'cust@example.com', 'phone': '1234567890', 'address': 'Test Address'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        customer_id = response.data['id']
        # List
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Retrieve
        url_detail = reverse('customer-detail', args=[customer_id])
        response = self.client.get(url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Update
        response = self.client.patch(url_detail, {'phone': '8888888888'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Delete
        response = self.client.delete(url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_product_crud(self):
        # Need a category and supplier first
        category = Category.objects.create(name='Cat1', description='Desc')
        supplier = Supplier.objects.create(name='Sup1', contact_email='sup1@example.com')
        url = reverse('product-list')
        data = {'name': 'Test Product', 'category': category.id, 'supplier': supplier.id, 'price': 10.0, 'stock': 5, 'description': 'Desc'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        product_id = response.data['id']
        # List
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Retrieve
        url_detail = reverse('product-detail', args=[product_id])
        response = self.client.get(url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Update
        response = self.client.patch(url_detail, {'stock': 10})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Delete
        response = self.client.delete(url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_order_crud(self):
        # Need a customer, supplier, category, product first
        customer = Customer.objects.create(name='Cust1')
        supplier = Supplier.objects.create(name='Sup2', contact_email='sup2@example.com')
        category = Category.objects.create(name='Cat2', description='Desc')
        product = Product.objects.create(name='Prod1', category=category, supplier=supplier, price=20.0, stock=10, description='Desc')
        url = reverse('order-list')
        data = {'order_type': 'sale', 'customer': customer.id, 'total': 20.0}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        order_id = response.data['id']
        # List
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Retrieve
        url_detail = reverse('order-detail', args=[order_id])
        response = self.client.get(url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Update
        response = self.client.patch(url_detail, {'total': 40.0})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Delete
        response = self.client.delete(url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
