from modeltranslation.translator import translator, TranslationOptions
from exp.models import KeySkill, KeySubSkill
from main.models import Quote, DesiredPosition


class KeySkillTranslationOptions(TranslationOptions):

    fields = ('name',)


class KeySubSkillTranslationOptions(TranslationOptions):

    fields = ('name',)


class QuoteTranslationOptions(TranslationOptions):

    fields = ('text',)

class DesiredPositionOptions(TranslationOptions):

    fields = ('name', 'description',)


translator.register(KeySkill, KeySkillTranslationOptions)
translator.register(KeySubSkill, KeySubSkillTranslationOptions)

translator.register(Quote, QuoteTranslationOptions)
translator.register(DesiredPosition, DesiredPositionOptions)
