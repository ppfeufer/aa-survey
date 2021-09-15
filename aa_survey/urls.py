"""
AA-Survey path config
"""

from django.urls import path

from aa_survey.constants import INTERNAL_URL_PREFIX
from aa_survey.views import management, survey

app_name: str = "aa_survey"

urlpatterns = [
    path("", survey.dashboard, name="survey_dashboard"),
    path("survey/<slug:survey_slug>/", survey.survey, name="survey_survey"),
    path(
        f"{INTERNAL_URL_PREFIX}/management/",
        management.dashboard,
        name="management_dashboard",
    ),
    path(
        f"{INTERNAL_URL_PREFIX}/management/<slug:survey_slug>/",
        management.dashboard,
        name="management_dashboard",
    ),
    path(
        f"{INTERNAL_URL_PREFIX}/ajax/get-survey-forms",
        management.ajax_get_survey_forms,
        name="management_ajax_get_survey_forms",
    ),
]
