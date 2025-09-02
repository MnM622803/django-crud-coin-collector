from django.contrib import admin
from .models import Coin, GlobalRank

class CoinAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'country', 'value', 'image')
    search_fields = ('name', 'country')

class GlobalRankAdmin(admin.ModelAdmin):
    list_display = ('coin', 'date', 'rank', 'source')
    search_fields = ('coin__name', 'source')

admin.site.register(Coin, CoinAdmin)
admin.site.register(GlobalRank, GlobalRankAdmin)