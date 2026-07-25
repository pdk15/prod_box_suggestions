from django.db import models

class Product(models.Model):
    name= models.CharField(max_length=100)
    length=models.FloatField()
    width=models.FloatField()
    height=models.FloatField()
    weight=models.FloatField()
    
    def __str__(self):
        return self.name
    


class ShippingBox(models.Model):
    
    name = models.CharField(max_length=100)

    inner_length = models.FloatField()
    inner_width = models.FloatField()
    inner_height = models.FloatField()

    max_weight = models.FloatField()

    cost = models.DecimalField(max_digits=8, decimal_places=2)

    def volume(self):
        return self.inner_length * self.inner_width * self.inner_height

    def __str__(self):
        return self.name
    
    
class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    
class OrderItem(models.Model):
    
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(default=1)
