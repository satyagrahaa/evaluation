#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from __future__ import unicode_literals

from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils.six import python_2_unicode_compatible


# from moneyfield import MoneyField




@python_2_unicode_compatible
class Property(models.Model):
    TYPE_RESIDENCIAL = 'R'
    TYPE_COMMERCIAL = 'C'
    TYPE_HOUSE = 'H'
    TYPE_LAND = 'L'

    TYPE_CHOICES = (
        (TYPE_RESIDENCIAL, _('Residencial')),
        (TYPE_COMMERCIAL, _('Commercial')),
        (TYPE_HOUSE, _('House')),
        (TYPE_LAND, _('Land')),
    )

    STATUS_VERIFIED = 'V'
    STATUS_PENDING = 'P'
    STATUS_REJECTED = 'R'

    STATUS_CHOICES = (
        (STATUS_VERIFIED, _('Verified')),
        (STATUS_PENDING, _('Pending')),
        (STATUS_REJECTED, _('Rejected')),
    )

    title = models.CharField(_('Title'), max_length=100)
    expiration_date = models.DateField(_('Expiration Date'))
    owner = models.CharField(_('Owner'), max_length=50)
    # price = MoneyField(_('Price'), max_digit=20, decimal_places=3,
    #                  currency_default=_('IRR'))
    type = models.CharField(_('Type'), max_length=1,choices=TYPE_CHOICES)
    image = models.ImageField(_('Image'), upload_to='/media/', blank=True, null=True)
    area_square_meter = models.PositiveIntegerField(_('Area in Square Meters'))
    verification_status = models.CharField(_('Verification Status'), max_length=1,
                                           choices=STATUS_CHOICES, default=STATUS_PENDING)
    elevator = models.BooleanField(_("Elevator"), default=False)

    def __str__(self):
        if self.title is not '':
            return self.title
        else:
            message = 'Untitled'
            return message

    class Meta(object):
        verbose_name = _('Property')
        verbose_name_plural = _('Properties')
