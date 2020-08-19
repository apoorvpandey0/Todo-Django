from django.db import models
from django.utils.timezone import now
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 500)
    completed_bool = models.BooleanField(default = False)
    created =  models.DateTimeField(default=now)
    completed = models.DateTimeField(default=now)
