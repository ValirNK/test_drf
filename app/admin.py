from django.contrib import admin
from .models import Food, FoodCategory


class CustomModelAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields if field.name != "id"]
        super(CustomModelAdmin, self).__init__(model, admin_site)

class FoodAdmin(CustomModelAdmin):
    model = 'Food'

class FoodCategoryAdmin(CustomModelAdmin):
    model = 'FoodCategory'

admin.site.register(Food, FoodAdmin)
admin.site.register(FoodCategory, FoodCategoryAdmin)
