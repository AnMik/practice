from django.db.models import *
from django.utils.timezone import now


class TimeStampedModel(Model):
    created = DateTimeField(auto_now_add=True, default=now)
    updated = DateTimeField(auto_now=True, default=now)

    class Meta:
        abstract = True