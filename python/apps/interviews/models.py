from django.contrib.auth import get_user_model
from django.db import models

from apps.candidates.models import Candidate
from apps.requests.models import Request

User = get_user_model()

INTERVIEW_STATUS = (
    (0, 'Предстоит'),
    (1, 'Прошло'),
    (2, 'Отменено'),
)


class Interview(models.Model):
    date = models.DateTimeField()
    status = models.IntegerField(default=1, choices=INTERVIEW_STATUS)
    candidate = models.ForeignKey(Candidate, on_delete=models.PROTECT)
    request = models.ForeignKey(Request, on_delete=models.PROTECT)
    reviewers = models.ManyToManyField(User)

    class Meta:
        default_related_name = 'interviews'
