from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
from .forms import UserCreationForm


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserCreationForm
    add_form = UserCreationForm

    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active','is_staff')})
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    
    search_fields = ('email', 'first_name', 'last_name')
    
    ordering = ('email', )







