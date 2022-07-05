from django.contrib import admin
from .models import Email


@admin.register(Email)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("email", "name",  "children", "with_children", "other_contacts", "other_qwestion", "created_at", "ip_address")



from django.contrib import admin

# Register your models here