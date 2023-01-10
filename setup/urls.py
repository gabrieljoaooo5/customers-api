from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from customers.views import CustomersViewSet

router = routers.DefaultRouter()
router.register('customers', CustomersViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
