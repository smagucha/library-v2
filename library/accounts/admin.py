# accounts.admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import User

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email','firstname','secondname','admin')
    list_filter = ('admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('firstname', 'secondname')}),
        ('Permissions', {'fields': ('admin','staff','active','groups', 'user_permissions')}),

    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','firstname', 'secondname','password1', 'password2',)}
        ),
    )
    search_fields = ('email', 'firstname', 'secondname')
    ordering = ('email', 'firstname', 'secondname')
    filter_horizontal = ()


admin.site.register(User, UserAdmin)

