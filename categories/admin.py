from django.contrib import admin
from .models import Brand,Category,SubCategory

class Brand_Column_Display(admin.ModelAdmin):
    list_display=('id','brand_name','short_description')
admin.site.register(Brand,Brand_Column_Display)

class Category_Column_Display(admin.ModelAdmin):
    list_display=('id','category_name','description','brand')
admin.site.register(Category,Category_Column_Display)

class SubCategory_Column_Display(admin.ModelAdmin):
    list_display=('id','subcategory_name','category')
admin.site.register(SubCategory,SubCategory_Column_Display)
