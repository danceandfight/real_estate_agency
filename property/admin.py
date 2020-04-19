from django.contrib import admin

from .models import Flat, Report_flat, Owner

class OwnerInline(admin.TabularInline):
    model = Flat.flats_owned_by.through
    raw_id_fields = ('owner',)
    extra = 0


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ['created_at']
    fieldsets = (
        ('Address', {
            'fields': (
                'town',
                'town_district',
                'address', 
                )
        }),
        ('Flats_characteristics', {
            'fields': (
                'new_building',
                'description',
                'price',
                'floor',
                'rooms_number',
                'living_area',
                'has_balcony',
                'construction_year',
                )
        }),
        (None, {
            'fields': (
                'active',
                'created_at',
                'liked_by')
        }),
    )
    list_display = (
                    'address',
                    'price',
                    'new_building',
                    'construction_year',
                    'town'
                    )
    list_editable = ['new_building']
    list_filter = [
                    'new_building',
                    'construction_year',
                    'town'
                    ]
    raw_id_fields = [
                    'liked_by'
                    ]
    inlines = [OwnerInline, ]

class Report_flatAdmin(admin.ModelAdmin):
    list_display = (
                    'user',
                    'flat',
                    'report_text'
                    )
    raw_id_fields = [
                    'flat'
                    ]

class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields =[
                    'flats_owned'
                    ]

admin.site.register(Flat, FlatAdmin)
admin.site.register(Report_flat, Report_flatAdmin)
admin.site.register(Owner, OwnerAdmin)
