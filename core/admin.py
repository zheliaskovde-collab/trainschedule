from django.contrib import admin
from .models import Station, Train, Route, RoutePoint

@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')

@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'total_seats')


class RoutePointInline(admin.TabularInline):
    model = RoutePoint
    extra = 1

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('train', 'price')
    inlines = [RoutePointInline]  