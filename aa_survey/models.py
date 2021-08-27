"""
Our models
"""

from sortedm2m.fields import SortedManyToManyField

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class General(models.Model):
    """
    Meta model for app permissions
    """

    class Meta:
        """
        Meta definitions
        """

        managed = False
        default_permissions = ()
        permissions = (
            ("basic_access", _("Can access the AA-Survey module")),
            (
                "manage_survey",
                _("Can manage the AA-Survey module"),
            ),
        )


class SurveyQuestion(models.Model):
    """
    Survey questions
    """

    title = models.CharField(max_length=254, verbose_name="Question")
    help_text = models.TextField(blank=True, null=True)
    multi_select = models.BooleanField(default=False)

    class Meta:
        """
        Meta definitions
        """

        default_permissions = ()

    def __str__(self):
        return "Question: " + self.title


class SurveyChoice(models.Model):
    """
    Survey choices
    """

    question = models.ForeignKey(
        SurveyQuestion, on_delete=models.CASCADE, related_name="choices"
    )
    choice_text = models.CharField(max_length=200, verbose_name="Choice")

    class Meta:
        """
        Meta definitions
        """

        default_permissions = ()

    def __str__(self):
        return self.choice_text


class SurveyForm(models.Model):
    """
    Survey forms
    """

    questions = SortedManyToManyField(SurveyQuestion)
    name = models.CharField(
        max_length=254, blank=True, null=True, verbose_name="Survey Name"
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        """
        Meta definitions
        """

        default_permissions = ()

    def __str__(self):
        return str(self.name)


class Survey(models.Model):
    """
    Surveys
    """

    form = models.ForeignKey(
        SurveyForm, on_delete=models.CASCADE, related_name="surveys"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="surveys")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Meta definitions
        """

        default_permissions = ()
        unique_together = ("form", "user")

    def __str__(self):
        return str(self.user) + " Survey " + str(self.form)

    @property
    def main_character(self):
        """
        Return the users main character
        :return:
        :rtype:
        """

        return self.user.profile.main_character

    @property
    def characters(self):
        """
        Return all characters for this user
        :return:
        :rtype:
        """

        return [o.character for o in self.user.character_ownerships.all()]


class SurveyResponse(models.Model):
    """
    Survey responses
    """

    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    survey = models.ForeignKey(
        Survey, on_delete=models.CASCADE, related_name="responses"
    )
    answer = models.TextField()

    class Meta:
        """
        Meta definitions
        """

        default_permissions = ()
        unique_together = ("question", "survey")

    def __str__(self):
        return str(self.survey) + " Answer To " + str(self.question)
