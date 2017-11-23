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

from django.conf.urls import url
from . import views

urlpatterns = [

    # ex: /library/
    url(r'^$', views.index, name='index'),

    # ex: /library/books/<ISBN>
    url(r'^books/(?P<ISBN>[0-9-A-Za-z]+)/$', views.book_detail, name='books'),
]
