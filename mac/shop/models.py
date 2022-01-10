from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    Price=models.IntegerField(default=0)
    product_name=models.CharField(max_length=50, default="")
    desc=models.CharField(max_length=300, default="")
    pub_date=models.DateField()
    image=models.ImageField(upload_to='shop/images',default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,default="")
    email=models.CharField(max_length=50,default="")
    phone=models.IntegerField(default=0)

    desc=models.CharField(max_length=300, default="")

    def __str__(self):
        return self.name


class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=5000, default="")
    name=models.CharField(max_length=50, default="")
    state=models.CharField(max_length=90, default="")
    email=models.CharField(max_length=50, default="")
    address=models.CharField(max_length=90, default="")
    city=models.CharField(max_length=90, default="")
    zip_code=models.CharField(max_length=90, default="")
    phone=models.CharField(max_length=15, default="")
    amount=models.IntegerField(default=0)

    class Meta:
        verbose_name_plural="Orders"

class OrderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default=0)
    update_desc=models.CharField(max_length=5000,default="")
    timestamp=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.update_desc[:7]+'...'
