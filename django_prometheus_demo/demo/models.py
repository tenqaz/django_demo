# Create your models here.
from django.db import models
from django_prometheus.models import ExportModelOperationsMixin


class User(ExportModelOperationsMixin('User'), models.Model):
    class Meta:
        db_table = 't_user'

    id = models.AutoField(primary_key=True)
    name = models.CharField()
    age = models.IntegerField()
    sex = models.CharField()
