from django.contrib import admin

from .models import Property


class PropertyAdmin(admin.ModelAdmin):

    list_display = [
        'title', 'owner', 'type', 'expiration_date', 'verification_status'
    ]
    list_filter = [
        'type', 'verification_status'
    ]
    fieldsets = (
        ('General Info:', {
            'fields': ['title', 'owner'],
        }),
        ('Specifications:', {
            'fields': ['type', 'area_square_meter', 'elevator'],
        }),
        ('Image', {
            'fields': ['image',],
        }),
        ('Expiration/Status', {
            'fields': [('expiration_date', 'verification_status'),],
        })
    )

admin.site.register(Property, PropertyAdmin)
