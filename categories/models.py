from django.db import models

# Brand Model
class Brand(models.Model):
    brand_name = models.CharField(max_length=1000,null=True,blank=True)
    short_description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.brand_name

# Category Model
class Category(models.Model):
    category_name = models.CharField(max_length=1000,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self): 
        return self.category_name

# Sub-Category Model
class SubCategory(models.Model):
    subcategory_name = models.CharField(max_length=1000,null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.subcategory_name
