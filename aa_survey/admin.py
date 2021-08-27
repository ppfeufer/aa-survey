"""
Django admin
"""

from django.contrib import admin

from aa_survey.models import SurveyChoice, SurveyForm, SurveyQuestion


class ChoiceInline(admin.TabularInline):
    """
    ChoiceInline
    """

    model = SurveyChoice
    extra = 0
    verbose_name_plural = "Choices (optional)"
    verbose_name = "Choice"


class QuestionAdmin(admin.ModelAdmin):
    """
    QuestionAdmin
    """

    fieldsets = [
        (None, {"fields": ["title", "help_text", "multi_select"]}),
    ]
    inlines = [ChoiceInline]


admin.site.register(SurveyQuestion, QuestionAdmin)
admin.site.register(SurveyForm)
