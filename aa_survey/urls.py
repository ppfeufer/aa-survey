"""
AA-Survey path config
"""

from django.urls import path

from aa_survey import views

app_name: str = "aa_survey"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
]
