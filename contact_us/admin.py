from django.contrib import admin
from .models import Contact_Us

class Contact_Us_Column_Display(admin.ModelAdmin):
    list_display=('id','name','email','reason','message','dates')
admin.site.register(Contact_Us,Contact_Us_Column_Display)
