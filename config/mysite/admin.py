from django.contrib import admin
from mysite.models import Quadro

# Register your models here.
class Quadros(admin.ModelAdmin):
    list_display = ('id','Nome')
    list_display_links = ('id', 'Nome')
    list_per_page = 20

admin.site.register(Quadro, Quadros)