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

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from trains.models import Reservation
from trains.serializers import ReservationSerializers

from rest_framework import status
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle


# Index page for rate limit challenge
def index(request):
    """
    Method for challenge description
    """
    pnr_numbers = Reservation.objects.values_list('PNR', flat=True)
    return render(request, 'trains/index.html', {'pnr_numbers': pnr_numbers})


# API view to get information of reservation status
@api_view(['POST'])
@throttle_classes([UserRateThrottle])
def get_status(request):
    """
    Get train status
    """
    if request.method == 'POST':
        if request.data:
            if 'PNR' in request.data.keys():
                pnr_requested = request.data['PNR']
                try:
                    reservation_detail = Reservation.objects.get(PNR=pnr_requested)
                    serializer = ReservationSerializers(reservation_detail)
                    return Response(serializer.data)
                except Reservation.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
