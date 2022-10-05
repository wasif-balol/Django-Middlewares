from django.db import models


class NewStats(models.Model):
    win = models.IntegerField()
    mac = models.IntegerField()
    iph = models.IntegerField()
    android = models.IntegerField()
    linux = models.IntegerField()
    oth = models.IntegerField()

    class Meta:
        verbose_name = "Stat"
        verbose_name_plural = "Stats"

    def __str__(self):
        return 'Stats Object'
