"""
The views
"""

from app_utils.logging import logger

from django.contrib import messages
from django.contrib.auth.decorators import (
    login_required,
    permission_required,
    user_passes_test,
)
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _

from aa_survey.models import Survey, SurveyForm, SurveyResponse


def check_for_main_character(user):
    return bool(user.profile.main_character)


@login_required
@user_passes_test(check_for_main_character)
@permission_required("aa_survey.basic_access")
def dashboard(request: WSGIRequest, form_id=None) -> HttpResponse:
    """
    Survey Dashboard view

    :param request:
    :type request:
    """

    if form_id:
        survey_form = get_object_or_404(SurveyForm, id=form_id)

        if request.method == "POST":
            try:
                Survey.objects.filter(user=request.user).filter(form=survey_form)

                logger.warning(
                    f"User {request.user} attempting to duplicate "
                    f'survey "{survey_form.name}'
                )

                messages.warning(
                    request,
                    mark_safe(
                        _("<h4>Warning!</h4><p>You have already taken this survey</p>")
                    ),
                )

                return redirect("aa_survey:dashboard")
            except Survey.DoesNotExist:
                survey = Survey(user=request.user, form=survey_form)
                survey.save()

                for question in survey_form.questions.all():
                    response = SurveyResponse(question=question, application=survey)

                    response.answer = "\n".join(
                        request.POST.getlist(str(question.pk), "")
                    )

                    response.save()

                logger.info(f'{request.user} took survey "{survey}"')

                messages.success(
                    request,
                    mark_safe(
                        _(
                            f"<h4>Success!</h4>"
                            f'<p>Thank you for your participation in the survey "{survey}"</p>'
                        )
                    ),
                )

                return redirect("aa_survey:dashboard")
        else:
            questions = survey_form.questions.all()

            return render(
                request,
                "hrapplications/create.html",
                context={"questions": questions, "survey_form": survey_form.name},
            )
    else:
        available_surveys = []
        for survey_form in SurveyForm.objects.all():
            if (
                not Survey.objects.filter(user=request.user)
                .filter(form=survey_form)
                .exists()
            ):
                available_surveys.append((survey_form.id, survey_form.name))

        return render(
            request,
            "aa_survey/view/dashboard.html",
            context={"available_surveys": available_surveys},
        )
