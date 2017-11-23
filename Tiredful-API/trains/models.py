# -*- coding: utf-8 -*-
#
#   ____  __  ___   ___  ___  ___  _  _  __       __   ___  __
#  (_  _)(  )(  ,) (  _)(   \(  _)( )( )(  )     (  ) (  ,\(  )
#   )(   )(  )  \  ) _) ) ) )) _) )()(  )(__    /__\  ) _/ )(
#  (__) (__)(_)\_)(___)(___/(_)   \__/ (____)  (_)(_)(_)  (__)
#
#
# Copyright (C) 2017-2018 Payatu Software Labs
# This file is part of Tiredful API application

from __future__ import unicode_literals

from django.db import models

WAITING = 'W'
CONFIRM = 'CNF'
RAC = 'RAC'
STATUS_CHOICES = (
    (WAITING, 'Waiting'),
    (CONFIRM, 'Confirm'),
    (RAC, 'RAC'),
)


class Reservation(models.Model):
    train_number = models.IntegerField()
    PNR = models.CharField(max_length=40)
    status = models.CharField(
        max_length=3,
        choices=STATUS_CHOICES,
        default=CONFIRM,
    )
