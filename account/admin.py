from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account,Client


class AccountAdmin(UserAdmin):
    list_display = ('email','first_name','last_name','date_joined','is_admin','is_verified')
    search_fields = ('email','username',)
    readonly_fields = ('date_joined','last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account,AccountAdmin)
admin.site.register(Client)