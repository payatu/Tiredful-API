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
from django.http import HttpResponse
from django.shortcuts import render

from intro.forms import LoginForm, LogoutForm


# Application index page.
def index(request):
    return render(request, 'intro/index.html', )


# About page.
def about(request):
    return render(request, 'intro/about.html')


# Scenarios page.
def scenario(request):
    return render(request, 'intro/scenarios.html')


# To manage user token
def handle_token(request):
    return render(request, 'intro/token.html', {'login_form': LoginForm(), 'logout_form': LogoutForm()})


# CSRF scenario
def csrf(request):
    return render(request, 'intro/csrf.html')
