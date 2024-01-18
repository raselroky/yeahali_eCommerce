from django.contrib import admin
from .models import Role_And_Permission,Action,Update_Message

class Role_And_Permission_Column_Display(admin.ModelAdmin):
    list_display=('id','group')
admin.site.register(Role_And_Permission,Role_And_Permission_Column_Display)

class Action_Column_Display(admin.ModelAdmin):
    list_display=('id','actions')
admin.site.register(Action,Action_Column_Display)

class Update_Message_Column_Display(admin.ModelAdmin):
    list_display=('id','message','time')
admin.site.register(Update_Message,Update_Message_Column_Display)