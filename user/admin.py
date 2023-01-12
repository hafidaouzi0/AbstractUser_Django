from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin
from .forms import NewUserForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.




fields=list(UserAdmin.fieldsets)
fields[1] = ('Personal Info',{'fields':('first_name','last_name','nickname','age')})
UserAdmin.fieldsets=tuple(fields)
admin.site.register(NewUser,UserAdmin)
