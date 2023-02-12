# -*- coding: utf-8 -*-

from django.contrib import admin
from . import models as api_models

admin.site.register(api_models.Peak)
