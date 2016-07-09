from django.contrib import admin

from .models import Employee, Attribute


class AttributeInline(admin.TabularInline):
    model = Attribute


class EmployeeAdmin(admin.ModelAdmin):
    inlines = [AttributeInline]


class AttributeAdmin(admin.ModelAdmin):
    # fields = ['employee', ('teamwork', 'discipline', 'spirit', 'creativity'), ]
    list_display = ['employee', 'teamwork', 'discipline', 'spirit', 'creativity',
                    'overall']
    ordering = ['-overall']
    fieldsets = (
        ('Employee evaluation', {
            'fields': ['employee', 'teamwork', 'discipline', 'spirit', 'creativity', ]
        }),
        ('View overall', {
            'classes': ('collapse',),
            'fields': ('overall',),
        }),
    )
    list_per_page = 10
    readonly_fields = ('overall',)
    save_on_top = True
    search_fields = ['employee__name']
    show_full_result_count = True

#
#     # radio_fields = {'employee': admin.VERTICAL}

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Attribute, AttributeAdmin)