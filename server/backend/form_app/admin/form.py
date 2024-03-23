from django.contrib import admin
from ..models.form import Form


@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")
