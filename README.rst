==========================
Cabot Webhook Alert Plugin
==========================

A plugin for `Cabot`_ service monitoring that will post alerts to a URL.

The plugin will POST a payload like the following to a user-defined endpoint::

    {
      'service': 'my_service_name',
      'status': 'ERROR',
      'old_status': 'PASSING',
    }


Installation
============

Install from pip::

    $ pip install cabot-alert-webhook
    $ foreman stop

Edit `conf/*.env`::

    # add cabot_alert_webhook to your comma separated list
    CABOT_PLUGINS_ENABLED=cabot_alert_webhook

Run migrations and restart cabot::

    $ foreman run python manage.py migrate
    $ foreman start

.. _Cabot: https://cabotapp.com
