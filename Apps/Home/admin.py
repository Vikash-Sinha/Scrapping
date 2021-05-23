from django.contrib import admin
from .models import *
from django.forms import forms
from django.urls import path
from django.shortcuts import redirect, render
import csv
# from import_export import resources
# from import_export.admin import ImportExportModelAdmin


class ScrappingDataAdmin(admin.ModelAdmin):
    list_per_page = 1000
    show_full_result_count = False
    list_display = [f.name for f in ScrappingData._meta.fields]


class DirectoryCategoryMasterResourceAdmin(ScrappingDataAdmin):
    resource_class = ScrappingDataAdmin
    list_per_page = 1000
    show_full_result_count = False
    list_display = [f.name for f in ScrappingData._meta.fields]


admin.site.register(ScrappingData, ScrappingDataAdmin)
