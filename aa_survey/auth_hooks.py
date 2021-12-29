"""
Hook into AA
"""

# Django
from django.utils.translation import ugettext_lazy as _

# Alliance Auth
from allianceauth import hooks
from allianceauth.services.hooks import MenuItemHook, UrlHook

# AA Survey
from aa_survey import __title__, urls
from aa_survey.views import survey


class AaSurveyMenuItem(MenuItemHook):  # pylint: disable=too-few-public-methods
    """
    This class ensures only authorized users will see the menu entry
    """

    def __init__(self):
        # Setup menu entry for sidebar
        MenuItemHook.__init__(
            self,
            _(__title__),
            "fas fa-poll-h fa-fw",
            "aa_survey:survey_dashboard",
            navactive=["aa_survey:"],
        )

    def render(self, request):
        """
        Check if the user has the permission to view this app
        :param request:
        :return:
        """

        if request.user.has_perm("aa_survey.basic_access"):
            count_available_surveys = survey.available_surveys_count(request=request)
            self.count = (
                count_available_surveys
                if count_available_surveys and count_available_surveys > 0
                else None
            )

            return MenuItemHook.render(self, request)

        return ""


@hooks.register("menu_item_hook")
def register_menu():
    """
    Register our menu item
    :return:
    """

    return AaSurveyMenuItem()


@hooks.register("url_hook")
def register_urls():
    """
    Register our base url
    :return:
    """

    return UrlHook(urls, "aa_survey", r"^surveys/")
