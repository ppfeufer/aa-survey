"""
Management views
"""

from django.contrib.auth.decorators import login_required, permission_required
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Count
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from aa_survey.helper.buttons import get_survey_management_action_buttons
from aa_survey.models import SurveyForm


@login_required
@permission_required("aa_survey.manage_survey")
def dashboard(request: WSGIRequest) -> HttpResponse:
    """
    Survey management
    :return:
    :rtype:
    """

    return render(request, "aa_survey/view/management.html")


@login_required
@permission_required("aa_survey.manage_survey")
def ajax_get_survey_forms(request: WSGIRequest) -> JsonResponse:
    """
    Ajax :: Get survey forms
    :param request:
    :type request:
    :return:
    :rtype:
    """

    data = list()
    survey_forms = (
        SurveyForm.objects.prefetch_related(
            "surveys",
        )
        .annotate(
            num_surveys=Count("surveys", distinct=True),
        )
        .order_by("pk")
    )

    for survey_form in survey_forms:
        survey_form_url = reverse(
            "aa_survey:survey_survey", kwargs={"survey_slug": survey_form.slug}
        )
        survey_form_name_html = f'<a href="{survey_form_url}">{survey_form.name}</a>'

        actions = get_survey_management_action_buttons(request, survey_form)

        data.append(
            {
                "name": survey_form.name,
                "name_html": {
                    "display": survey_form_name_html,
                    "sort": survey_form.name,
                },
                "description": survey_form.description,
                "count": survey_form.num_surveys,
                "actions": actions,
            }
        )

    return JsonResponse(data, safe=False)


@login_required
@permission_required("aa_survey.manage_survey")
def result(request: WSGIRequest, survey_slug: str) -> HttpResponse:
    """
    Surves result
    :param request:
    :type request:
    :param survey_slug:
    :type survey_slug:
    """

    survey_form = (
        SurveyForm.objects.prefetch_related(
            "surveys", "surveys__responses", "surveys__responses__question"
        )
        .filter(slug__exact=survey_slug)
        .annotate(
            num_surveys=Count("surveys", distinct=True),
        )
        .order_by("pk")
        .get()
    )

    context = {"survey_form": survey_form}

    return render(request, "aa_survey/view/management/result.html", context)
