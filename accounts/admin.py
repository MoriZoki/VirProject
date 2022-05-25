from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

# add phone to personal info 
UserAdmin.fieldsets[1][1]['fields'] = ('first_name', 'last_name', 'email', 'phone')

# add is vip and vip end time to permission field 
UserAdmin.fieldsets[2][1]['fields'] = ('is_active',
'is_staff',
'is_superuser',
'is_vip',
'vip_end_time',
'groups',
'user_permissions',)



UserAdmin.list_display += ('is_vip',)

admin.site.register(User, UserAdmin)
