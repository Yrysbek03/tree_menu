from django.contrib import admin

from menu.models import Menu


class AdminMenu(admin.ModelAdmin):

    def get_fields(self, request, obj=None):
        if obj:
            return 'name', 'parent', 'description'
        else:
            return 'name', 'parent', 'description'


admin.site.register(Menu, AdminMenu)
