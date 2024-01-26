from django.contrib import admin
from .models import Event, Category_Evenement, Registration


class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "date_time", "location", "category")
    list_filter = ("date_time", "category")
    search_fields = ("title", "description")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name", "description")


admin.site.register(Event, EventAdmin)
admin.site.register(Category_Evenement, CategoryAdmin)
