from django.contrib import admin
from customers.models import Customer

class Customers(admin.ModelAdmin):
    list_display = ('id', 'name', 'email','cpf', 'phone', 'active')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('active',)
    list_editable = ('active',)
    list_per_page = 25

admin.site.register(Customer, Customers)

