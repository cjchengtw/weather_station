# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 19:47:14 2017

@author: User
"""

import os 
BASE_DIR = os.path.dirname(os.path.dirname(__file__)) 
DATABASES = { 
    'default': { 
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), 
    } 
} 
DEBUG = True 