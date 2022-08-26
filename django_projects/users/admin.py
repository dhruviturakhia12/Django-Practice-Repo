from django.contrib import admin
from users.models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea


class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'user_name', 'first_name','last_name')
    list_filter = ('email', 'user_name', 'first_name','last_name',)
    ordering = ('-start_date',)
    list_display = ('email', 'user_name', 'first_name','last_name',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name','last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active',)}),
        ('Personal', {'fields': ('birth_date', 'about', 'age',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'user_name', 'first_name','last_name', 'password1', 'password2', 'is_active', 'is_staff', 'about', 'age',
                'birth_date')}
         ),
    )


admin.site.register(NewUser, UserAdminConfig)
