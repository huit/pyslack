# pyslack

A package to facilitate the use of a slack webhook for notifications.

## Slack setup

Setup of a webhook in Slack is required.
See <a href="https://api.slack.com/messaging/webhooks">https://api.slack.com/messaging/webhooks

## Installation and Usage

    - requires python >=3.7

    pip install https://github.com/huit/pyslack/archive/v1.0.1.tar.gz

    from pyslack.notify import NotificationService 

    ns = NotificationService(webhook="<unique_id_for_slack_webhook>", username="<notification_username>", icon_emoji="<emoji>")
    
    ns.success("SUCCESS TITLE") # only title required for success message
    ns.info(title="INFO TITLE", message="informational message")
    ns.warning(title="WARNING TITLE", message="warning message")
    ns.error(title="ERROR TITLE", message="error message", link="https://www.example.com", link_title="Example.com")

### Instantiation Notes
1. <unique_id_for_slack_webhook> must be supplied by slack, and will be appended to "https://hooks.slack.com/services/"
1. <notification_username> can be any string, not necessarily an existing slack user
1. <emoji> must be a valid slack emoji name - do not include any ':' as it will automatically be wrapped ":<emoji>:"
    
### Parameters
1. title -> REQUIRED
1. message -> REQUIRED ( defaults to 'Success!' for .success() )
1. link -> OPTIONAL ( must be a fully formed URL, e.g., https://www.example.com )
1. link_title -> OPTIONAL ( if link parameter is supplied but not link_title, link_title defaults to 'link' )

## Examples

<img width="384" alt="pyslack_examples" src="https://user-images.githubusercontent.com/6807526/110037044-debd6b00-7d0b-11eb-93e6-9d5ed344073f.png">
