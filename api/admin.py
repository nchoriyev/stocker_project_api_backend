from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Staffs, Services, ServicesCategory, Blog, Applications, About

@admin.register(Staffs)
class StaffsAdmin(ImportExportModelAdmin):
    list_display = ['id', 'username', 'email', 'status_choices', 'slug']
    list_display_links = ['id', 'username', 'email', 'status_choices', 'slug']
    search_fields = ['username', 'email', 'status_choices', 'slug']
    ordering = ['id']
    prepopulated_fields = {'slug': ('username',)}


@admin.register(Services)
class ServicesAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name', 'category', 'status', 'views', 'slug']
    list_display_links = ['id', 'name', 'category', 'status', 'views', 'slug']
    search_fields = ['name', 'category', 'status', 'slug']
    ordering = ['id']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ServicesCategory)
class ServicesCategoryAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name', 'status', 'slug']
    list_display_links = ['id', 'name', 'status', 'slug']
    search_fields = ['name', 'status', 'slug']
    ordering = ['id']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Blog)
class BlogAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name', 'status', 'admin', 'slug']
    list_display_links = ['id', 'name', 'status', 'admin', 'slug']
    search_fields = ['name', 'status', 'admin', 'slug']
    ordering = ['id']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Applications)
class ApplicationsAdmin(ImportExportModelAdmin):
    list_display = ['id', 'full_name', 'email', 'telephone_number', 'status', 'slug']
    list_display_links = ['id', 'full_name', 'email', 'telephone_number', 'status', 'slug']
    search_fields = ['full_name', 'email', 'telephone_number', 'status', 'slug']
    ordering = ['id']
    prepopulated_fields = {'slug': ('full_name',)}


@admin.register(About)
class AboutAdmin(ImportExportModelAdmin):
    list_display = ['id', 'our_status', 'telephone_number', 'status', 'slug']
    list_display_links = ['id', 'our_status', 'telephone_number', 'status', 'slug']
    search_fields = ['our_status', 'telephone_number', 'status', 'slug']
    ordering = ['id']
    prepopulated_fields = {'slug': ('our_status',)}
