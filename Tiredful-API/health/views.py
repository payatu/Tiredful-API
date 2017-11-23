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
from django.db import connection
from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from health.models import Tracker
from health.serializers import TrackerSerializers


# Index method for Blog article listing
def index(request):
    """
    Index page for health application
    """
    tracker_details = Tracker.objects.all()
    return render(request, 'health/index.html', {'tracker_details': tracker_details})


# get user activities
@api_view(['POST'])
def get_activity(request):
    """
    Details of user activity monthwise
    """
    if request.method == 'POST':
        if request.data:
            if 'month' in request.data.keys():
                month_requested = request.data['month']
                try:
                    activity_detail = Tracker.objects.raw(
                        'Select * from health_tracker where month=%s' % month_requested)
                    final_serialized_data = []
                    for activity in activity_detail:
                        serializer = TrackerSerializers(activity)
                        final_serialized_data.append(serializer.data)
                    return Response(final_serialized_data)
                except Tracker.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                except ValueError:
                    cursor = connection.cursor()
                    cursor.execute('Select * from health_tracker where month=%s' % month_requested)
                    activity_detail = cursor.fetchall()
                    return JsonResponse(activity_detail, safe=False)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
