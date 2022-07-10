from django.db import models

# Create your models here.
class AttributeName(models.Model):
    id = models.IntegerField(primary_key=True)
    nazev = models.CharField(max_length = 255,null=True, blank=True)
    kod = models.CharField(max_length = 255,null=True, blank=True)
    zobrazit = models.BooleanField(null=True, blank=True)
    

class AttributeValue(models.Model):
    id = models.IntegerField(primary_key=True)
    hodnota = models.CharField(max_length = 255,blank=True, null=True)

class Attribute(models.Model):
    id = models.IntegerField(primary_key=True)
    nazev_atributu_id = models.ForeignKey('AttributeName', on_delete=models.CASCADE)
    hodnota_atributu_id = models.ForeignKey('AttributeValue', on_delete=models.CASCADE)
    

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    nazev = models.CharField(max_length = 255,blank=True, null=True)
    description = models.CharField(max_length = 255,blank=True, null=True)
    cena = models.CharField(max_length = 255,blank=True, null=True)
    mena = models.CharField(max_length = 255,blank=True, null=True)
    published_on = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(blank=True, null=True)
    

class ProductAttributes(models.Model):
    id = models.IntegerField(primary_key=True)
    attribute = models.ForeignKey('Attribute', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    
    
class ProductImage(models.Model):
    id = models.IntegerField(primary_key=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    obrazek_id = models.ForeignKey('Image', on_delete=models.CASCADE)
    nazev = models.CharField(max_length = 255,blank=True, null=True)
    
    
class Image(models.Model):
    id = models.IntegerField(primary_key=True)
    nazev = models.CharField(max_length = 255,blank=True, null=True)
    obrazek = models.CharField(max_length = 2048,blank=True, null=True)
    

class Catalog(models.Model):
    id = models.IntegerField(primary_key=True)
    nazev = models.CharField(max_length = 255,blank=True, null=True)
    obrazek_id = models.ForeignKey('Image', on_delete=models.CASCADE)
    products_ids = models.ManyToManyField(Product,blank=True)
    attributes_ids = models.ManyToManyField(Attribute,blank=True)
    
    