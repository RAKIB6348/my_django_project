from django.contrib import admin
from .models import AcademicYear, Section, Subject, SchoolClass


@admin.register(AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin):
    list_display = ('year', 'is_active', 'created')
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
    list_display = ('name', 'created')
    search_fields = ('name',)
    ordering = ('name',)

    fieldsets = (
        ('Section Info', {
            'fields': ('name',)
        }),
    )


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'created')
    search_fields = ('name', 'code')
    ordering = ('code',)

    fieldsets = (
        ('Subject Info', {
            'fields': ('name', 'code')
        }),
    )


@admin.register(SchoolClass)
class SchoolClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'class_code', 'created')
    search_fields = ('name', 'class_code')
    ordering = ('name',)

    fieldsets = (
        ('Class Info', {
            'fields': ('name', 'class_code')
        }),
    )