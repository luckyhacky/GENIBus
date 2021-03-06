#!/usr/bin/env python
# -*- coding: utf-8 -*-

__copyright__ = """
Grundfos GENIBus Library.

(C) 2007-2017 by Christoph Schueler <github.com/Christoph2,
                                     cpu12.gems@googlemail.com>

 All Rights Reserved

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""
__author__  = 'Christoph Schueler'
__version__ = '0.1.0'

import six

def hexDump(data):
    if six.PY3:
        return ', '.join(["0x{:02x}".format(x) for x in data])
    else:
        return ', '.join(["0x{:02x}".format(ord(x)) for x in data])

def wordToBytes(w):
    return tuple(((w & 0xff00) >> 8, w & 0xff))


#flatten = lambda l: [item for sublist in l for item in sublist]

