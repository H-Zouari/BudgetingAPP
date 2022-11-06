from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Account, Income, Payment

# Register your models here.
admin.site.register(Account)
admin.site.register(Payment)
admin.site.register(Income)