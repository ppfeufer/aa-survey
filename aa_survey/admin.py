"""
Django admin
"""

# Django
from django.contrib import admin

# AA Survey
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
        (None, {"fields": ["title", "help_text", "mandatory", "multi_select"]}),
    ]
    inlines = [ChoiceInline]


admin.site.register(SurveyQuestion, QuestionAdmin)


@admin.register(SurveyForm)
class SurveyFormAdmin(admin.ModelAdmin):
    """
    SurveyForm admin
    """

    list_display = ("name", "description", "open_until", "is_active")
    exclude = ("slug",)
