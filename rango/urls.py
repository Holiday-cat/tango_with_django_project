# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 10:22:44 2023

@author: yiqin
"""

from django.urls import path
from rango import views
from django.conf import settings 
from django.conf.urls.static import static


app_name = 'rango'

'''
urlpatterns = [
    path('', views.index, name='index'),
]
'''
urlpatterns = [ 
    path('', views.index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


