# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 09:27:14 2021

@author: mfors
"""


def get_credentials():
        username = input('Type username: ')
        password = input('Type password: ')
        return username, password
    
username, password = get_credentials()
print(username, password)