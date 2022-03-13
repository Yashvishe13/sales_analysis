from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=100, null=False, blank=False)
    product_price = models.IntegerField()
    product_category = models.CharField(max_length=100, null=False, blank=False)
 
    def __str__(self):
        return f'{self.product_name} - {self.product_price} - {self.product_category}'   

class Customer(models.Model):
    customer_name = models.CharField(max_length=100, null=False, blank=False)
    customer_gender = models.CharField(max_length=100, null=False, blank=False)
    customer_age = models.IntegerField()
    customer_number = models.IntegerField()
    product = models.ManyToManyField(Product)

    def __str__(self):
        return f'{self.customer_name} - {self.customer_gender} - {self.customer_age} - {self.customer_number}'    

class Transactions(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    def __str__(self):
        return f'{self.quantity}'