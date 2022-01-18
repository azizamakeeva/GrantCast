from django.contrib import admin
from apps.grants.models import Category, Grant, Location, Discipline

admin.site.register(Category)
admin.site.register(Grant)
admin.site.register(Location)
admin.site.register(Discipline)
