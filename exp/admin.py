from django.contrib import admin
from .models import KeySkill, KeySubSkill
from modeltranslation.admin import TranslationAdmin


class KeySkillAdmin(TranslationAdmin):

    list_display = ('name', )

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
        (None, { 'fields': ['name', 'icon', 'activeColor']})
    ]
    

class KeySubSkillAdmin(TranslationAdmin):

    list_display = ('name', 'key_skill', )

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
        (None, { 'fields': ['name', 'icon']}),
        ("Parent", {'fields': ['key_skill']})
    ]

admin.site.register(KeySkill, KeySkillAdmin)
admin.site.register(KeySubSkill, KeySubSkillAdmin)
