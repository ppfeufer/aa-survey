"""
Our models
"""

# Third Party
from sortedm2m.fields import SortedManyToManyField

# Django
from django.contrib.auth.models import User
from django.db import models, transaction
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

# AA Survey
from aa_survey.constants import INTERNAL_URL_PREFIX
from aa_survey.managers import SurveyFormManager


def _generate_slug(MyModel: models.Model, name: str) -> str:
    """
    Generate a valid slug and return it.
    :param MyModel:
    :type MyModel:
    :param name:
    :type name:
    :return:
    :rtype:
    """

    if name == INTERNAL_URL_PREFIX:
        name = "hyphen"

    run = 0
    slug_name = slugify(name, allow_unicode=True)

    while MyModel.objects.filter(slug=slug_name).exists():
        run += 1
        slug_name = slugify(f"{name}-{run}", allow_unicode=True)

    return slug_name


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
    mandatory = models.BooleanField(default=False)

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

    is_active = models.BooleanField(default=True)
    questions = SortedManyToManyField(SurveyQuestion)
    name = models.CharField(
        max_length=254,
        blank=False,
        null=False,
        verbose_name="Survey Name",
        help_text="Give your survey a good and descriptive name",
    )
    description = models.TextField(
        blank=False,
        null=False,
        verbose_name="Survey Description",
        help_text="Quick description what this survey is about ...",
    )
    open_until = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Available until",
        help_text=(
            "This survey is available until (Eve Time) ... (Optional: If no date is "
            "set, the survey will be available until it is no longer marked as active.)"
        ),
    )
    slug = models.SlugField(max_length=254, unique=True, allow_unicode=True)

    objects = SurveyFormManager()

    class Meta:
        """
        Meta definitions
        """

        default_permissions = ()
        ordering = ["-pk"]

    def __str__(self):
        return str(self.name)

    @transaction.atomic()
    def save(self, *args, **kwargs):
        """
        Generate slug for new objects and update first and last messages.
        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        """

        if self._state.adding is True or self.slug == INTERNAL_URL_PREFIX:
            self.slug = _generate_slug(type(self), self.name)

        super().save(*args, **kwargs)


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
