# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 02:57:12 2017

@author: User
"""

from django import forms

class Contact(forms.Form):
    user_name = forms.CharField(label="您的姓名", max_length=50)
    user_email = forms.CharField(label="電子信箱", max_length=30)
    user_contact = forms.CharField(label="您的意見",widget=forms.Textarea)
    
    