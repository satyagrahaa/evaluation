from __future__ import unicode_literals
from django.core.validators import MaxValueValidator
from django.db import models


# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=20)
    job_title = models.CharField(max_length=40)
    img = models.CharField(max_length=500)

    #python 2 str compatible
    #python 2_unicode
    def __str__(self):
        return self.name

# limits att values
class Attribute(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    teamwork = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(10, 'Enter value between 0-10')])
    spirit = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(10, 'Enter value between 0-10')])
    discipline = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(10, 'Enter value between 0-10')])
    creativity = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(10, 'Enter value between 0-10')])

    def __str__(self, string=None):
        string = '%s >>> Teamwork: %d Spirit: %d Discipline: %d Creativity: %d' \
            % (self.employee, self.teamwork, self.spirit, self.discipline, self.creativity)
        return string

"""
def validate_max(value):
    if value > 100:
        raise ValidationError(
            _('%(value)s should be at most 100'),
            params={'value': value},
        )

        """


# 0-submit to git 0.5 - flake8 1-date 2-order by employee nae 3-filter by date
# add to admin: admin in-line, list display, search fileds, ordering