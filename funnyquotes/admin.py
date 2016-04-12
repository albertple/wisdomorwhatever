from django.contrib import admin
from funnyquotes.models import *

class FamousQuoteAdmin(admin.ModelAdmin):
	list_display = ('quote', 'author')

class InfamousQuoteAdmin(admin.ModelAdmin):
	display = ('add')

# Register your models here.
admin.site.register(FamousQuote, FamousQuoteAdmin)
admin.site.register(InfamousQuote, InfamousQuoteAdmin)