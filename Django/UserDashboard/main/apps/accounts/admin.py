from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
from .forms import UserRegistrationForm

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserRegistrationForm
    add_form = UserRegistrationForm

    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_admin')
    list_filter = ('is_active', 'is_staff', 'is_admin')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active','is_staff', 'is_admin')})
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    
    search_fields = ('email', 'first_name', 'last_name')
    
    ordering = ('email', )







