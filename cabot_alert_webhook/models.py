from cabot.cabotapp.alert import AlertPlugin, AlertPluginUserData
from django import forms
from os import environ as env
import requests
import json

from logging import getLogger
logger = getLogger(__name__)

class WebhookAlertUserData(AlertPluginUserData):
    name = "Webhook Plugin"
    webhook_url = models.URLField()

class WebhookAlertPlugin(AlertPlugin):
    name = "Webhook"
    slug = "cabot_alert_webhook"
    author = "Rockerbox"
    version = "0.0.1"
    font_icon = "fa fa-rocket"

    def send_alert(self, service, users, duty_officers):
        message = service.get_status_message()
        for u in users:
            post_to_url = u.cabot_alert_webhook_settings.webhook_url
            logger.info(message)
            if post_to_url:
                requests.post(
                    u.cabot_alert_webhook_settings.webhook_url,
                    data=json.dumps({'message': message})
                )
        return True
