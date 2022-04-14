from django import VERSION

from multiselectfield.db.fields import MultiSelectField  # noqa: F401
from multiselectfield.forms.fields import MultiSelectFormField  # noqa: F401

# default_app_config was deprecated in Django 3.2.
if VERSION < (3, 2):
    default_app_config = 'multiselectfield.apps.MultiSelectFieldConfig'
