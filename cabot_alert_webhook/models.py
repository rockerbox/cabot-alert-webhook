from cabot.cabotapp.alert import AlertPlugin
from cabot.cabotapp.alert import AlertPluginUserData
from django.db import models
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

        webhook_urls = [u.webhook_url for u in WebhookAlertUserData.objects.filter(user__user__in=users)]

        for url in webhook_urls:
            logger.info(message)
            requests.post(
                url,
                data=json.dumps({'message': message})
            )
        return True
