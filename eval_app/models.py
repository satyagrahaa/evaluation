#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from __future__ import unicode_literals

from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.six import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


# Create your models here.

@python_2_unicode_compatible
class Employee(models.Model):
    name = models.CharField(_('Name'), max_length=20)
    job_title = models.CharField(_('Job Title'), max_length=40, blank=True, null=True)

    # python 2 str compatible
    # python 2_unicode
    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Attribute(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT,
                                 verbose_name=_('Employee'))
    teamwork = models.PositiveIntegerField(_('Teamwork'), default=0, validators=[
        MaxValueValidator(10, 'Enter value between 0-10')])
    spirit = models.PositiveIntegerField(_('Spirit'), default=0, validators=[
        MaxValueValidator(10, 'Enter value between 0-10')])
    discipline = models.PositiveIntegerField(_('Discipline'), default=0, validators=[
        MaxValueValidator(10, 'Enter value between 0-10')])
    creativity = models.PositiveIntegerField(_('Creativity'), default=0, validators=[
        MaxValueValidator(10, 'Enter value between 0-10')])
    overall = models.PositiveIntegerField(_('Overall'))

    def save(self, *args, **kwargs):
        self.overall = self.teamwork + self.spirit + self.discipline + self.creativity
        super(Attribute, self).save(*args, **kwargs)

    def __str__(self, string=None):
        info = {
            'employee': self.employee, 'teamwork': self.teamwork,
            'spirit': self.spirit, 'discipline': self.discipline,
            'creativity': self.creativity
        }

        string = ("%(employee)s >>> Teamwork: %(teamwork)d "
                  "Spirit: %(spirit)d Discipline: %(discipline)d "
                  "Creativity: %(creativity)d") % info
        return string


"""

"""

# 0-submit to git 0.5 - flake8 1-date 2-order by employee nae 3-filter by date
# add to admin: admin in-line, list display, search fileds, ordering
