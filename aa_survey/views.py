"""
The views
"""

from django.contrib.auth.decorators import login_required, permission_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render


@login_required
@permission_required("aa_survey.basic_access")
def index(request: WSGIRequest) -> HttpResponse:
    """
    Survey Dashboard view

    :param request:
    :type request:
    """

    context = {}

    return render(request, "aa_survey/view/dashboard.html", context)
