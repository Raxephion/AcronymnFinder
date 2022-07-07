# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 11:53:03 2022

@author: Pierre-Henri Rossouw

"60 Apps in 60 Days Challenge - App #1: Create Acronymns"

"""

u_input=str(input("Enter a phrase/sentence: "))
usertxt=u_input.split()
a=" "
for i in usertxt:
    a=a+str(i[0]).upper()
    print(a)

