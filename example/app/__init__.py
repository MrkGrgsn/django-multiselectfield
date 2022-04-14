from django import VERSION

# default_app_config was deprecated in Django 3.2.
if VERSION < (3, 2):
    default_app_config = 'app.apps.AppAppConfig'
