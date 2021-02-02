from django.db import models


class TableFirst(models.Model):
    field_first = models.TextField(verbose_name='First field')


class TableSecond(models.Model):
    field_second = models.TextField(verbose_name='Second field')
    table_first = models.ForeignKey('TableFirst', models.CASCADE)
