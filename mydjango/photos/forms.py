# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 19:47:58 2022

@author: pei-chen
"""

from django import forms
from .models import Photo

class UploadModelForm(forms.ModelForm):
    class Meta:
        model=Photo
        fields=('image',)#這是欄位
        widgets={
            'image':forms.FileInput(attrs={'class':"form-control-file"})
            }