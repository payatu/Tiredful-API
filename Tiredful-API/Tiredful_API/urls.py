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

"""Tiredful_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib.auth.models import User, Group

from rest_framework import permissions, routers, serializers, viewsets


# first we define the serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group


urlpatterns = [
    # URL for user login
    url(r'^oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    # URL for including intro app.
    url(r'', include('intro.urls', namespace="intro")),

    # URL for including library app
    url(r'^api/v1/', include('library.urls', namespace="library-api")),
    url(r'^library/', include('library.urls', namespace="library")),

    # URL for including exams app
    url(r'^api/v1/', include('exams.urls', namespace="exams-api")),
    url(r'^exams/', include('exams.urls', namespace="exams")),

    # URL for including blog app
    url(r'^api/v1/', include('blog.urls', namespace="blog-api")),
    url(r'^blog/', include('blog.urls', namespace="blog")),

    # URL for including trains app
    url(r'^api/v1/', include('trains.urls', namespace="trains-api")),
    url(r'^trains/', include('trains.urls', namespace="trains")),

    # URL for including health app
    url(r'^api/v1/', include('health.urls', namespace="health-api")),
    url(r'^health/', include('health.urls', namespace="health")),

    # URL for including advertisements app
    url(r'^api/v1/', include('advertisements.urls', namespace="advertisements-api")),
    url(r'^advertisements/', include('advertisements.urls', namespace="advertisements")),

]
