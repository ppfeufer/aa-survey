"""
Managers for our models
"""

from django.db import models
from django.db.models import Q
from django.utils import timezone


class SurveyFormQuerySet(models.QuerySet):
    def available(self) -> models.QuerySet:
        """
        Filter boards that given user has access to.
        """

        # If not a forum manager, check if the user has access to the board
        return self.filter(
            (Q(open_until__gte=timezone.now()) | Q(open_until__isnull=True)),
            Q(is_active__iexact=1),
        ).distinct()


class SurveyFormManagerBase(models.Manager):
    """
    BoardManagerBase
    """

    pass


SurveyFormManager = SurveyFormManagerBase.from_queryset(SurveyFormQuerySet)