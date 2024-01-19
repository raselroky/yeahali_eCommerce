from django.db import models
from categories.models import Brand,Category,SubCategory
from user_management.models import Registration_All


class Add_Product(models.Model):
    #user=models.ForeignKey(Registration_All,on_delete=models.CASCADE,null=True,blank=True,help_text='which is uploading product for selling')
    product_name=models.CharField(max_length=1000,null=True,blank=True)
    product_description=models.TextField(null=True,blank=True,help_text='shortly full details for product and explain size,color,qunatity etc')
    product_brand=models.ForeignKey(Brand,on_delete=models.CASCADE,null=True,blank=True)
    product_category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    product_subcategory=models.ForeignKey(SubCategory,on_delete=models.CASCADE,null=True,blank=True)
    product_image=models.FileField(upload_to='product_image/',null=True,blank=True)
    product_price=models.TextField(null=True,blank=True)
    contact_me=models.TextField(null=True,blank=True,help_text='email, number, social_link or any details for contact')
    upload_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

#multiple image 
class Image_Upload(models.Model):
    product=models.ForeignKey(Add_Product,on_delete=models.CASCADE,null=True,blank=True,related_name='images')
    product_image=models.ImageField(upload_to="product_image/",null=True,blank=True)

    def __str__(self):
        return self.product.product_name
    