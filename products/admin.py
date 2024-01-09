from django.contrib import admin
from .models import Add_Product,Image_Upload

class Image_Upload_Column_Display(admin.ModelAdmin):
    list_display=('id','product','product_image')
admin.site.register(Image_Upload,Image_Upload_Column_Display)

class Add_Product_Column_Display(admin.ModelAdmin):
    list_display=('id','product_name','product_description','product_brand','product_category','product_subcategory','product_image','product_price','contact_me','upload_time')
admin.site.register(Add_Product,Add_Product_Column_Display)
