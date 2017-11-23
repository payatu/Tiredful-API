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
from base64 import b64encode, b64decode

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from exams.models import ScoreCard
from exams.serializers import ScoreCardSerializer


# Index for insecure direct object reference scenario
def index(request):
    """
    For insecure direct object reference challenge and login form
    """
    return render(request, 'exams/index.html', )


# Score detail of exam
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_score(request, score_card):
    """
    Details of exam score card.
    """
    try:
        score_card = (b64decode(score_card))
    except TypeError:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    try:
        exam = ScoreCard.objects.get(pk=score_card)
    except ScoreCard.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ScoreCardSerializer(exam)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
