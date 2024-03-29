"""
App config
"""

# Django
from django.apps import AppConfig

# AA Survey
from aa_survey import __version__


class AaSurveyConfig(AppConfig):
    """
    Application config
    """

    name = "aa_survey"
    label = "aa_survey"
    verbose_name = f"Survey v{__version__}"
