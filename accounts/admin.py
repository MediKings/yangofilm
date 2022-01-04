from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from  django.contrib.auth import get_user_model


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'phone', 'password')}),
        (_('Personnal Info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions')}),
        (_('Importants dates'), {'fields': ('last_login', 'date_joined')}),
    )

    """For new User"""
    add_fieldsets =(
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone', 'password1', 'password2'),
        }),
    ) 
    list_display = ('first_name', 'last_name','email', 'phone', 'is_staff')
    search_fields = ('email', 'phone', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(get_user_model(), CustomUserAdmin)
