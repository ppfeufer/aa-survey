"""
Helper for rendering bootstrap buttons
"""

from django.contrib.auth.decorators import login_required, permission_required
from django.core.handlers.wsgi import WSGIRequest

from aa_survey.models import SurveyForm


@login_required
@permission_required("aa_survey.manage_survey")
def get_survey_management_action_buttons(
    request: WSGIRequest, survey_form: SurveyForm
) -> str:
    """
    Get the action buttons for the management dashboard view table
    :param request:
    :type request:
    :param survey_form:
    :type survey_form:
    :return:
    :rtype:
    """

    survey_results = '<a class="btn btn-info btn-sm btn-aa-survey" href=""><i class="fas fa-poll-h"></i></a>'
    close_survey = '<button class="btn btn-warning btn-sm btn-aa-survey"><i class="fas fa-lock"></i></button>'
    delete_survey = '<button class="btn btn-danger btn-sm btn-aa-survey"><i class="far fa-trash-alt"></i></a>'

    return_value = survey_results + close_survey + delete_survey

    return return_value
