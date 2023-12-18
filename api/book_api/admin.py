from django.contrib import admin
from .models import Kitap

@admin.register(Kitap)
class KitapAdmin(admin.ModelAdmin):
    list_display = ('kitapid','kitapad','yazarid_kitap','yayintarihi','dil','ozet','kategoriid_kitap','sayfasayisi')
