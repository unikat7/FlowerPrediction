from django.contrib import admin
from .models import IrisModel

# Register your models here.

@admin.register(IrisModel)
class IrisDataAdmin(admin.ModelAdmin):
    list_display = ("sepal_length", "sepal_width", "petal_length", "petal_width", "species")

