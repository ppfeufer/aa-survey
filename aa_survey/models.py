"""
Our models
"""

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
