from django.contrib import admin
from .models import BaseProduct

class BaseProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'external_id', 'get_active']
    actions = ['activate_baseproduct', 'deactivate_baseproduct']

    @admin.display(description='active', boolean=True)
    def get_active(self, obj):
        return bool(obj.is_active)

    @admin.action(description='Activate selected produtc(s)')
    def activate_baseproduct(self, request, queryset):
        queryset.update(is_active=True)
    
    @admin.action(description='Deactivate selected produtc(s)')
    def deactivate_baseproduct(self, request, queryset):
        queryset.update(is_active=True)

admin.site.register(BaseProduct, BaseProductAdmin)
