from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User  



class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_admin', 'is_active')
    search_fields = ('email',)
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ('last_login',)
    fieldsets = ()

    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    ordering = ('email',)


admin.site.register(User, UserAdmin)


