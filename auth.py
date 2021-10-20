# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 09:27:14 2021

@author: mfors
"""

import json

#all branches stuff

print('This should show up in both branches')

def get_credentials():
    """input user credentials"""
    username = input('Type username: ')
    password = input('Type password: ')
    return username, password
    
def authenticate(username, password, pwdb):
    auth = False
    if username in pwdb:
        if password == pwdb[username]:
            print('Authentication successful!')
            auth = True
        else:
            print('Wrong password!')
    else:
        add_user(username, password, pwdb)
    return auth

def add_user(username, password, pwdb):
    response = input('Do you want to create a new user? [y/n]')
    if response == 'y':
        pwdb[username] = password
        write_pwdb(pwdb)
    else: 
        print('User not added')
        #add new user
        raise NotImplementedError('Why are you so lazy?')
    

def write_pwdb(pwdb):
    with open('pwdb.json', 'wt') as pwdb_file:
        json.dump(pwdb, pwdb_file)
    print('Pwdb written!')
# with: context, this will open the file and close it afterwards. 'wt' is for write text
    
def read_pwdb():
    with open('pwdb.json', 'rt') as pwdb_file:
        pwdb = json.load(pwdb_file)
    return pwdb
# 'rt' for read text


username, password = get_credentials()
pwdb = read_pwdb()
authenticate(username, password, pwdb)
