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

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'off'}))
    grant_type = forms.CharField(widget=forms.HiddenInput(attrs={'value': 'password'}))
    client_id = forms.CharField(widget=forms.HiddenInput(attrs={'value': 'ALGGN0UmsY2Gb9cs3V4CEKMfpBJ2D2XZQXuTFfND'}))
    client_secret = forms.CharField(widget=forms.HiddenInput(attrs={
        'value': 'mWM7pgvjtUSAtfaK8RXLjzOaLmurBxIWxMdQIQ0t1fSv9orqOnYr5wP5CaFN8DE18NiFiKKalQPu1WecmpbfoZCGYhMqMACz6i2WkWYs5E8gjXxqekjCyPkhBmO5n5EN'}))


class LogoutForm(forms.Form):
    token = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    client_id = forms.CharField(widget=forms.HiddenInput(attrs={'value': 'ALGGN0UmsY2Gb9cs3V4CEKMfpBJ2D2XZQXuTFfND'}))
    client_secret = forms.CharField(widget=forms.HiddenInput(attrs={
        'value': 'mWM7pgvjtUSAtfaK8RXLjzOaLmurBxIWxMdQIQ0t1fSv9orqOnYr5wP5CaFN8DE18NiFiKKalQPu1WecmpbfoZCGYhMqMACz6i2WkWYs5E8gjXxqekjCyPkhBmO5n5EN'}))
