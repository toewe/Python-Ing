#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created in 2020

@author: Herold
"""

def anzahl_zeichen(text):
    """
    Diese Funktion bestimmt die Anzahl der Zeichen in einem Text.
    """
    return len(str(text))

def anzahl_woerter(text, sep=' '):
    """
    Diese Funktion bestimmt die Anzahl der Wörter in einem Text.
    """
    return len(str(text).split(sep))

def anzahl_vokale(text, y = False):
    """
    Diese Funktion bestimmt die Anzahl der Vokale in einem Text.
    """
    vokale = 'aeiouäöü'
    if y: vokale += 'y'
    return len([_ for _ in str(text).lower() if _ in vokale])
    
def anzahl_konsonanten(text, y = True):
    """
    Diese Funktion bestimmt die Anzahl der Konsonanten in einem Text.
    """
    konsonanten = 'bcdfghjklmnpqrstvwxz'
    if y: konsonanten += 'y'
    return len([_ for _ in str(text).lower() if _ in konsonanten])

lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, \
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris \
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in \
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla \
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in \
culpa qui officia deserunt mollit anim id est laborum. Curabitur \
pretium tincidunt lacus. Nulla gravida orci a odio. Nullam varius, \
turpis et commodo pharetra, est eros bibendum elit, nec luctus magna \
felis sollicitudin mauris. Integer in mauris eu nibh euismod gravida. \
Duis ac tellus et risus vulputate vehicula. Donec lobortis risus a \
elit. Etiam tempor. Ut ullamcorper, ligula eu tempor congue, eros \
est euismod turpis, id tincidunt sapien risus a quam. Maecenas fermentum \
consequat mi. Donec fermentum. Pellentesque malesuada nulla a mi. Duis \
sapien sem, aliquet nec, commodo eget, consequat quis, neque. Aliquam \
aucibus, elit ut dictum aliquet, felis nisl adipiscing sapien, sed \
malesuada diam lacus eget erat. Cras mollis scelerisque nunc. Nullam \
arcu. Aliquam consequat. Curabitur augue lorem, dapibus quis, laoreet \
et, pretium ac, nisi. Aenean magna nisl, mollis quis, molestie eu, \
feugiat in, orci. In hac habitasse platea dictumst.'

pi = 'Pi.'

e = 'E.'

hallo = 'Guten Tag.'
