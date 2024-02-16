from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE


class Cure(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=30)
    price = models.IntegerField(null=False)
    description = models.TextField(max_length=70)
    amount = models.IntegerField()
    cure_location = models.TextField(null=False, default='On the shelf', )
    available = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)


class Customer(User):
    def __str__(self):
        return self.customer_first_name

    customer_first_name = models.CharField(max_length=50, blank=True)
    customer_last_name = models.CharField(max_length=150, blank=True)
    customer_email = models.EmailField(blank=True)
    birth_date = models.DateField(blank=True)


class Role(models.Model):
    def __str__(self):
        return self.role_name

    role_name = models.CharField(max_length=20, null=False, unique=True)


class Staff(User):
    def __str__(self):
        return self.staff_username

    staff_username = models.CharField(max_length=50, null=False, unique=True)
    role = models.ForeignKey(Role, on_delete=CASCADE)
    is_deleted = models.BooleanField(default=False)


class Order(models.Model):
    def __str__(self):
        return str(self.id)

    customer = models.ForeignKey(Customer, on_delete=CASCADE)
    order_date = models.DateField(auto_now_add=True)
    status = models.TextField(max_length=50, blank=True)


class OrderItem(models.Model):
    def __str__(self):
        return str(self.id)

    order = models.ForeignKey(Order, on_delete=CASCADE)
    cure = models.ForeignKey(Cure, on_delete=CASCADE)
    quantity = models.IntegerField(null=False)


class CustomerCure(models.Model):
    customer = models.ForeignKey(Customer, on_delete=CASCADE)
    cure = models.ForeignKey(Cure, on_delete=CASCADE)
