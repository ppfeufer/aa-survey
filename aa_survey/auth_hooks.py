"""
Hook into AA
"""

from django.utils.translation import ugettext_lazy as _

from allianceauth import hooks
from allianceauth.services.hooks import MenuItemHook, UrlHook

from aa_survey import __title__, urls


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
            "aa_survey:dashboard",
            navactive=["aa_survey:"],
        )

    def render(self, request):
        """
        Check if the user has the permission to view this app
        :param request:
        :return:
        """

        if request.user.has_perm("aa_survey.basic_access"):
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

    return UrlHook(urls, "aa_survey", r"^survey/")
