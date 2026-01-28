from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active','employee_no','first_name', 'last_name', 'mobile_no')
    list_filter = ('email', 'is_staff', 'is_active','employee_no','first_name', 'last_name', 'mobile_no')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'mobile_no')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'mobile_no', 'last_name', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.site_header = 'Real_time_attendance'
admin.site.site_title = 'Real_time_attendance'
admin.site.index_title = 'Feature Areas'
