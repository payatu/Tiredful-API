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
import json

from rest_framework import status

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from blog.models import Article
from blog.serializers import ArticleSerializer
from blog.permissions import UserPermission


# Index method for Blog article listing
def index(request):
    """
    Index page for blog application - To list all blogs
    """
    Articles = Article.objects.all().values('id', 'title')
    return render(request, 'blog/index.html', {'articles': Articles})


# Method to display article
@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes((UserPermission,))
def article(request, article_id):
    """
    Display particular blog article, delete particular blog article, update blog article
    """
    try:
        selected_article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        if selected_article.approval_status:
            serializer = ArticleSerializer(selected_article)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        if 'HTTP_ISADMIN' in request.META:
            if request.META['HTTP_ISADMIN'] == "True":
                selected_article.delete()
                return Response(json.dumps('Successfully deleted'))
            else:
                return Response(json.dumps('Invalid header value'))
        else:
            return Response(json.dumps('IsAdmin header missing'))
    elif request.method == 'PATCH':
        selected_article.approval_status = True
        selected_article.save()
        return Response(json.dumps('{Message: Approved successfully}'))
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


# Method for approving the blog
@api_view(['GET'])
@permission_classes((IsAdminUser,))
def approve_article(request, article_id):
    """
    Approve article for displaying
    """
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        article.approval_status = True
        article.save()
        return Response(json.dumps('{Message: Approved successfully}'))
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
