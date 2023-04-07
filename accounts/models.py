from django.db import models

# Create your models here.

class Customer(models.Model):

    name=models.CharField(max_length=200,null='true')
    phone=models.CharField(max_length=200,null='true')
    email=models.CharField(max_length=200,null='true')
    date_created=models.DateTimeField(auto_now_add='true')

    def __str__(self):
        return self.name +" "+self.phone

class Tag(models.Model):

    name=models.CharField(max_length=200,null='true') 
    def __str__(self):
        return self.name      

class Product(models.Model):
    Category=(
        ('indoor','indoor'),
        ('outdoor','outdoor')
    )

    name=models.CharField(max_length=200,null='true')
    price=models.FloatField(null='true')
    category=models.CharField(max_length=200,null='true',choices=Category)
    date_created=models.DateTimeField(auto_now_add='true')
    tag=models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.name
        

class Order (models.Model):
    Status=(
        ('pending','pending'),
        ('delivered','delivered'),
        ('out for delivery','out for delivery')
    )
    customer=models.ForeignKey(Customer,null='true',on_delete=models.SET_NULL)
    product=models.ForeignKey(Product,null='true',on_delete=models.SET_NULL)
    status=models.CharField(max_length=200,null='true',choices=Status)
    date_created=models.DateTimeField(auto_now_add='true')

    def __str__(self) -> str:
        print(self.customer)
        return f"{self.product}"

    