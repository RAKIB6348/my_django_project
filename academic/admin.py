from django.contrib import admin
from .models import AcademicYear, Section


@admin.register(AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin):
    list_display = ('year', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('year',)
    ordering = ('-year',)

    fieldsets = (
        ('Academic Year Info', {
            'fields': ('year', 'is_active')
        }),
    )


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

    fieldsets = (
        ('Section Info', {
            'fields': ('name',)
        }),
    )