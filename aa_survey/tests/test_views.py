from django.test import TestCase
from django.urls import reverse

from aa_survey.tests.utils import create_fake_user

VIEWS_PATH = "aa_survey.views"


class TestIndexViews(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        # User cannot access forum
        cls.user_1001 = create_fake_user(1002, "Peter Parker")

        # User can access forum
        cls.user_1002 = create_fake_user(
            1001, "Bruce Wayne", permissions=["aa_survey.basic_access"]
        )

        # User can manage forum
        cls.user_1003 = create_fake_user(
            1003,
            "Clark Kent",
            permissions=["aa_survey.basic_access", "aa_survey.manage_survey"],
        )

    # def setUp(self) -> None:
    #     # board 1 has an unread topic
    #     self.board_1 = Board.objects.create(name="Physics", category=self.category)
    #     topic_1 = Topic.objects.create(subject="Mysteries", board=self.board_1)
    #     create_fake_messages(topic_1, 4)
    #     topic_1.update_last_message()
    #     topic_2 = Topic.objects.create(subject="Recent Discoveries", board=self.board_1)
    #     create_fake_messages(topic_2, 2)
    #     topic_2.update_last_message()
    #     LastMessageSeen.objects.create(
    #         topic=topic_2,
    #         user=self.user_1001,
    #         message_time=topic_2.messages.order_by("-time_posted")[0].time_posted,
    #     )
    #     self.board_1.update_last_message()
    #
    #     # board 2 has no unread topics
    #     self.board_2 = Board.objects.create(name="Math", category=self.category)
    #     topic = Topic.objects.create(subject="Unsolved Problems", board=self.board_2)
    #     create_fake_messages(topic, 2)
    #     topic.update_last_message()
    #     LastMessageSeen.objects.create(
    #         topic=topic,
    #         user=self.user_1001,
    #         message_time=topic.messages.order_by("-time_posted")[0].time_posted,
    #     )
    #     self.board_2.update_last_message()

    def test_should_show_dashboard(self):
        # given
        self.client.force_login(self.user_1002)

        # when
        res = self.client.get(reverse("aa_survey:dashboard"))

        # then
        self.assertEqual(res.status_code, 200)
