from django.contrib import admin
from pharma.models import Cure, Customer, Role, Staff, Order, OrderItem, CustomerCure

admin.site.register(Cure)
admin.site.register(Customer)
admin.site.register(Role)
admin.site.register(Staff)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(CustomerCure)
