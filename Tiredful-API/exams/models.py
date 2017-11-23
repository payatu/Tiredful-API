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


# Exam scorecard
class ScoreCard(models.Model):
    exam = models.CharField(max_length=40)
    user = models.ForeignKey(User)
    total_marks = models.DecimalField(max_digits=5, decimal_places=2)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    attempt_number = models.IntegerField(default=0)
    question_attempted = models.IntegerField(default=0)
    question_correct = models.IntegerField(default=0)
    question_wrong = models.IntegerField(default=0)
