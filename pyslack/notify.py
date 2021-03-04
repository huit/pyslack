import requests
import json

DEFAULT_USERNAME = "Python Slack Notifications"
DEFAULT_ICON_EMOJI = "slack"


class NotificationService:
    """
    Provides convenience methods for formatting of different types of messages sent to slack,
    including success(), info(), warning(), and error()
    """

    COLOR_SUCCESS = "#00b600"
    COLOR_INFO = "#7799b9"
    COLOR_ERROR = "#ef0000"
    COLOR_WARNING = "#ffce03"

    ICON_SUCCESS = "white_check_mark"
    ICON_INFO = "information_source"
    ICON_ERROR = "x"
    ICON_WARNING = "warning"

    def __init__(self, webhook: str, username: str = DEFAULT_USERNAME, icon_emoji: str = DEFAULT_ICON_EMOJI):
        """
        Includes configuration for successful setup to use slack webhook
        webhook is the only required parameter - others will default
        :param webhook: REQUIRED - must be set up in Slack
        :param username: OPTIONAL - defaults to 'Python Slack Notifications'
        :param icon_emoji: OPTIONAL - defaults to 'slack'
        """
        self.webhook = webhook
        self.username = username
        self.icon_emoji = icon_emoji

    BASE_SLACK_URL = "https://hooks.slack.com/services/"

    def slack_payload_with_attachments(self, attachments):
        return json.dumps({
            "username": self.username,
            "icon_emoji": f":{self.icon_emoji}:",
            "unfurl_links": True,
            "attachments": attachments
        })

    @property
    def slack_url(self):
        return self.BASE_SLACK_URL + self.webhook

    @staticmethod
    def setup_fallback(icon, title, link=None, link_title="link"):
        """
        helper method
        :param icon:
        :param title:
        :param link: OPTIONAL
        :param link_title: OPTIONAL - if link is supplied, link_title defaults to 'link'
        :return:
        """
        if link and link_title:
            fallback = f" :{icon}: *{title}*: (<{link}|{link_title}>)"
        else:
            fallback = f" :{icon}: *{title}*"
        return fallback

    @staticmethod
    def setup_attachments(color: str, fallback: str, message: str):
        """
        helper method - all parameters required for successful configuration of payload
        :param color:
        :param fallback:
        :param message:
        :return:
        """
        return [
            {
                "fallback": fallback,
                "color": color,
                "fields": [
                    {
                        "value": f"{fallback}\n{message}",
                        "short": False
                    }
                ]
            }
        ]

    def success(self, title: str, message: str = "Success!", link: str = None, link_title: str = None):
        """
        Sends success message using COLOR_SUCCESS and ICON_SUCCESS
        :param title:
        :param message:
        :param link:
        :param link_title:
        :return:
        """
        fallback = self.setup_fallback(self.ICON_SUCCESS, title, link, link_title)
        attachments = self.setup_attachments(self.COLOR_SUCCESS, fallback, message)
        requests.post(self.slack_url,
                      data={"payload": self.slack_payload_with_attachments(attachments)})

    def info(self, title: str, message: str, link: str = None, link_title: str = None):
        """
        Sends informational message using COLOR_INFO and ICON_INFO
        :param title:
        :param message:
        :param link:
        :param link_title:
        :return:
        """

        fallback = self.setup_fallback(self.ICON_INFO, title, link, link_title)
        attachments = self.setup_attachments(self.COLOR_INFO, fallback, message)
        requests.post(self.slack_url,
                      data={"payload": self.slack_payload_with_attachments(attachments)})

    def error(self, title: str, message: str, link: str = None, link_title: str = None):
        """
        Sends error message using COLOR_ERROR and ICON_ERROR
        :param title:
        :param message:
        :param link:
        :param link_title:
        :return:
        """

        fallback = self.setup_fallback(self.ICON_ERROR, title, link, link_title)
        attachments = self.setup_attachments(self.COLOR_ERROR, fallback, message)
        requests.post(self.slack_url,
                      data={"payload": self.slack_payload_with_attachments(attachments)})

    def warning(self, title: str, message: str, link: str = None, link_title: str = None):
        """
        Sends informational message using COLOR_WARNING and ICON_WARNING
        :param title:
        :param message:
        :param link:
        :param link_title:
        :return:
        """
        fallback = self.setup_fallback(self.ICON_WARNING, title, link, link_title)
        attachments = self.setup_attachments(self.COLOR_WARNING, fallback, message)
        requests.post(self.slack_url,
                      data={"payload": self.slack_payload_with_attachments(attachments)})
