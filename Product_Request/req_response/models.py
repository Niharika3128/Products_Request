from django.db import models

class Product_details(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_description = models.TextField(max_length=100)
    created_date = models.DateTimeField()
    created_by = models.CharField(max_length=50,default='Admin')
    product_image = models.FileField(upload_to='products/')

class User_details(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    address = models.TextField(max_length=200)
    contact_no = models.IntegerField()
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)