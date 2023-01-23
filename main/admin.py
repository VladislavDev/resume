from django.contrib import admin
from .models import Quote, DesiredPosition, ExRates
from modeltranslation.admin import TranslationAdmin


class QuoteAdmin(TranslationAdmin):

    list_display = ('text', )

    class Media:
        js = (
            '/static/jquery-3.6.1.min.js',
            '/static/jquery-ui.min.js',
            '/static/modeltranslation/js/force_jquery.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }

    fieldsets = [
        (None, {'fields': ['text']})
    ]


class DesiredPositionAdmin(TranslationAdmin):

    list_display = ('name', 'salary_rub', 'isActive', )

    class Media:
        js = (
            '/static/jquery-3.6.1.min.js',
            '/static/jquery-ui.min.js',
            '/static/modeltranslation/js/force_jquery.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }

    fieldsets = [
        ('Translatable', {'fields': ['name', 'description']}),
        ('Use rules', {'fields': ['isActive']}),
        ('Salary', {'fields': ['salary_rub', 'salary_usd']}),
        ('Media', {'fields': ['banner']})
    ]


class ExRatesAdmin(admin.ModelAdmin):

    def actualTime(self, obj):
        return obj.updated.strftime("%d.%m.%Y %H:%M")

    def rubRate(self, obj):
        return obj.rateRub

    actualTime.short_description = 'Updated'
    rubRate.short_description = 'RUB'

    list_display = ('actualTime', 'rubRate', )

admin.site.register(Quote, QuoteAdmin)
admin.site.register(DesiredPosition, DesiredPositionAdmin)
admin.site.register(ExRates, ExRatesAdmin)