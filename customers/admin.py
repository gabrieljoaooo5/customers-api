from django.contrib import admin
from customers.models import Customer

class Customers(admin.ModelAdmin):
    list_display = ('id', 'name', 'email','cpf', 'phone', 'active')
    list_display_links = ('id', 'name')
    search_fields = ('name','cpf',)
    list_filter = ('active',)
    list_editable = ('active',)
    list_per_page = 25
    ordering = ('name',)

admin.site.register(Customer, Customers)

