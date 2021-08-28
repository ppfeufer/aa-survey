"""
AA-Survey path config
"""

from django.urls import path

from aa_survey import views
from aa_survey.constants import INTERNAL_URL_PREFIX

app_name: str = "aa_survey"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path(
        f"{INTERNAL_URL_PREFIX}/management/",
        views.management_dashboard,
        name="management_dashboard",
    ),
    path("survey/<slug:survey_slug>/", views.survey, name="survey"),
]
