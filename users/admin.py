from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()

# customize user view in django admin
class UserAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name','email',)
    list_display = ('first_name','last_name','last_login','is_active',)

# Register your models here.
admin.site.register(User, UserAdmin)

admin.site.site_header = 'Budgeting Admin'
admin.site.site_title = 'Budgeting'