"""
AA-Forum path config
"""

from django.urls import path

from aa_survey import views

app_name: str = "aa_survey"

# IMPORTANT
# All internal URLs need to start with the designated prefix
# to prevent conflicts with user generated forum URLs

urlpatterns = [
    path("", views.index, name="dashboard"),
]
