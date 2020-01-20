# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 15:34:25 2020

@author: usuario
"""

from django.urls import path
from . import views

urlpatterns=[
        path('',views.post_list,name='post_list'),
        ]
 