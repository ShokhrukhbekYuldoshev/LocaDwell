from django.contrib import admin
from .models import CustomUser

admin.site.site_header = "Locadwell Admin"
admin.site.site_title = "Locadwell Admin Portal"
admin.site.index_title = "Welcome to Locadwell Portal"

# Register your models here.
admin.site.register(CustomUser)
