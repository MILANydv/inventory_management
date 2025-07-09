from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, CustomerViewSet, OrderViewSet,
                    ProductViewSet, SupplierViewSet)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = router.urls 