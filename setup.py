#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='cabot-alert-webhook',
      version='0.0.1',
      description='A Webhook plugin for Cabot',
      author='Rockerbox',
      author_email='engineering@rockerbox.com',
      url='https://github.com/rockerbox/cabot-alert-webhook',
      packages=find_packages(),
      download_url = 'https://github.com/rockerbox/cabot-alert-webhook/tarball/master',
      bugtrack_url = "https://github.com/rockerbox/cabot-alert-webhook/issues",
      keywords = ['cabot', 'webhook', 'status check'],
     )
