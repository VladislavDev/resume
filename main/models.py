from django.db import models
from django.db.models import F, ExpressionWrapper

from django.contrib import admin
from django.utils.timezone import now

from ckeditor.fields import RichTextField
from decimal import Decimal


class Quote(models.Model):

    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text


class PositionManager(models.Manager):

    def updateSalaryUSD(self, rate):

        DesiredPosition.objects.update(salary_usd = ExpressionWrapper(F('salary_rub') / Decimal(rate), output_field=models.DecimalField()))


class DesiredPosition(models.Model):

    name = models.CharField(max_length=100)
    banner = models.ImageField(upload_to='position-baners', default=None)
    description = RichTextField(null=True, blank=True)
    isActive = models.BooleanField(default = False)

    salary_rub = models.DecimalField(max_digits=9, decimal_places=2)
    salary_usd = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    objects = PositionManager()

    @admin.display(
        boolean = True
    )

    def __str__(self):
        return self.name


class RateManager(models.Manager):

    def add(self, rate):
        
        try:
            newRate = self.create(updated=now(), rateRub=rate)
            return newRate
        except Exception as e:
            # TODO Create ExceptionCollector
            print(e)


class ExRates(models.Model):

    updated = models.DateTimeField('actual')
    rateRub = models.DecimalField(max_digits=9, decimal_places=6)

    objects = RateManager()

    def __str__(self):
        return "Exchange rate on " + str(self.updated.strftime("%d.%m.%Y %H:%M"))