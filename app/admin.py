from django.contrib.auth.models import User, Group
from django.contrib import admin

from app.models import Product, Category

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'price', 'discount', 'image', 'is_expensive')
    list_filter = ('category', 'price')

    def is_expensive(self, obj):
        return obj.price > 50_000

    is_expensive.boolean = True

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

admin.site.register(Category)




admin.site.unregister(User)
admin.site.unregister(Group)