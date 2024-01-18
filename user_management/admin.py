from django.contrib import admin
from .models import Registration_All,Blacklisted

class Registration_All_Column_Display(admin.ModelAdmin):
    list_display=('id','first_name','last_name','email','mobile','address','date_of_joining','role','image','gender','marital_status','blood_group','soacial_link','date_of_birth','company_name','company_address','company_contact_number','company_logo','bank_name','card_or_account_number','branch_name')
admin.site.register(Registration_All,Registration_All_Column_Display)

class Blacklisted_Column_Display(admin.ModelAdmin):
    list_display=('id','email','is_active','try_count','wrong_password')
admin.site.register(Blacklisted,Blacklisted_Column_Display)