"""
Tests for view.py
"""

# Django
from django.test import TestCase
from django.urls import reverse

# AA Survey
from aa_survey.tests.utils import create_fake_user

VIEWS_PATH = "aa_survey.views"


class TestViews(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        """
        Set up groups and users
        """

        super().setUpClass()

        # User cannot access survey module
        cls.user_1001 = create_fake_user(1002, "Peter Parker")

        # User can access survey module
        cls.user_1002 = create_fake_user(
            1001, "Bruce Wayne", permissions=["aa_survey.basic_access"]
        )

        # User can manage survey module
        cls.user_1003 = create_fake_user(
            1003,
            "Clark Kent",
            permissions=["aa_survey.basic_access", "aa_survey.manage_survey"],
        )

    def test_should_show_survey_dashboard(self):
        """
        Test that a user with basic_access can see the survey module
        :return:
        :rtype:
        """

        # given
        self.client.force_login(self.user_1002)

        # when
        res = self.client.get(reverse("aa_survey:survey_dashboard"))

        # then
        self.assertEqual(res.status_code, 200)

    def test_should_not_show_survey_dashboard(self):
        """
        Test that a user without basic_access can't see the survey module
        :return:
        :rtype:
        """

        # given
        self.client.force_login(self.user_1001)

        # when
        res = self.client.get(reverse("aa_survey:survey_dashboard"))

        # then
        self.assertIsNot(res.status_code, 200)

    def test_should_show_management_dashboard(self):
        """
        Test that a user with manage_survey can see the management dashboard
        :return:
        :rtype:
        """

        # given
        self.client.force_login(self.user_1003)

        # when
        res = self.client.get(reverse("aa_survey:management_dashboard"))

        # then
        self.assertEqual(res.status_code, 200)

    def test_should_not_show_management_dashboard(self):
        """
        Test that a user without manage_survey can't see the management dashboard
        :return:
        :rtype:
        """

        # given
        self.client.force_login(self.user_1002)

        # when
        res = self.client.get(reverse("aa_survey:management_dashboard"))

        # then
        self.assertIsNot(res.status_code, 200)
