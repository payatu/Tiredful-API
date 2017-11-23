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
from django.contrib.auth.models import User


# Fitness Tracker
class Tracker(models.Model):
    sleep = models.DecimalField(max_digits=5, decimal_places=2)
    heartbeat = models.IntegerField()
    calories = models.DecimalField(max_digits=7, decimal_places=2)
    running = models.DecimalField(max_digits=5, decimal_places=2)
    month = models.IntegerField()
    user = models.ForeignKey(User)
