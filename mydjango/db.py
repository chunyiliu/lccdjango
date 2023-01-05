# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 20:53:05 2022

@author: pei-chen
"""

import pymysql

dbsetting={
    "host":"127.0.0.1",
    "port":3306,
    "user":"root",
    "password":"123456789",
    "db":"mydjango",
    "charset":"utf8"
    }

conn=pymysql.connect(**dbsetting)