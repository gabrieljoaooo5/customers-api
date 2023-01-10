from django.contrib import admin
from django.urls import re_path, include
from rest_framework import routers
from customers.views import CustomersViewSet

router = routers.DefaultRouter()
router.register('customers', CustomersViewSet)

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('', include(router.urls)),
]