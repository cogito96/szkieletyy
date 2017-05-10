from django.contrib import admin

from .models import Zawodnik
from .models import Zespol
from .models import TypZdarzenia
from .models import Mecz

class ZawodnikAdmin(admin.ModelAdmin):
    fields = ['imie', 'nazwisko', 'pozycja', 'data_urodzenia', 'zespol']

admin.site.register(Zawodnik,ZawodnikAdmin)

class ZespolAdmin(admin.ModelAdmin):
    fields = ['nazwa_klubu', 'trener', 'prezes', 'strona_internetowa']

admin.site.register(Zespol,ZespolAdmin)

class MeczAdmin(admin.ModelAdmin):
    fields = ['zespol_gospodarz','zespol_gosc','bramki_gospodarz','bramki_gosc','data','kolejka']

admin.site.register(Mecz,MeczAdmin)

class TypZdarzeniaAdmin(admin.ModelAdmin):
    fields = ['nazwa']

admin.site.register(TypZdarzenia,TypZdarzeniaAdmin)
