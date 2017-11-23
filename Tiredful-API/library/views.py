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
import traceback, sys

from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from library.models import Book
from library.serializers import BookSerializer


# API for showing book details - leaking system information
@api_view(['GET'])
def book_detail(request, ISBN):
    """
    Get details of specific book
    """
    try:
        book = Book.objects.get(ISBN=ISBN)
    except Book.DoesNotExist:
        if ISBN.isupper():
            return Response(traceback.format_exception(*sys.exc_info()))
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def index(request):
    """
    Index page for information disclosure challenge
    """
    books = Book.objects.all()
    return render(request, 'library/index.html', {'books': books})
