from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True) # auto_now every time we update the product object this property sets time to that date/time
#                                                     auto_now_add - with this only time when we create Product will be stored
class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)

class Order(models.Model):
    placed_at = models.DateTimeField(auto_now_add=True)
    PENDING_STATUS = 'P'
    COMPLETE_STATUS = 'C'
    FAILED_STATUS = 'F'

    PAYMENT_STATUS_CHOICES = [
        (PENDING_STATUS, 'Pending'),
        (COMPLETE_STATUS, 'Complete'),
        (FAILED_STATUS, 'Failed'),
    ]

    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PENDING_STATUS)


# One-to-One database relationship
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)