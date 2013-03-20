#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
##
## Grundfos GENIBus Library for Arduino.
##
## (C) 2007-2013 by Christoph Schueler <github.com/Christoph2,
##                                      cpu12.gems@googlemail.com>
##
##  All Rights Reserved
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License along
## with this program; if not, write to the Free Software Foundation, Inc.,
## 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
##
##

import wx


class MultipleChoiceButtons(wx.Panel):
    def __init__(self, parent, buttons, label = '', horizontal = True, default = None):
        wx.Panel.__init__(self, parent = parent, id = wx.ID_ANY)

        staticBox = wx.StaticBox(self, label = ' %s ' % label.strip())
        groupSizer = wx.StaticBoxSizer(staticBox)

        sizer = wx.BoxSizer(wx.HORIZONTAL if horizontal else wx.VERTICAL)

        self.buttonDict = dict()

        for buttonName in buttons:
            btnID = wx.NewId()
            btn = wx.ToggleButton(parent, label = buttonName, id = btnID)
            btn.Bind(wx.EVT_TOGGLEBUTTON, self.buttonClicked)
            sizer.Add(btn, 1, wx.ALL, 5)
            self.buttonDict[buttonName] = btn

        if not default:
            default = buttons[0]
        self._activeButton = self.buttonDict[default]
        self._activeButton.SetValue(True)
        self._handler = None

        groupSizer.Add(sizer)
        self.SetSizerAndFit(groupSizer)


    def setHandler(self, handler):
        self._handler = handler

    def callHandler(self, value):
        if self._handler:
            self._handler(value)

    def buttonClicked(self, event):
        button = event.GetEventObject()
        self.setActiveButton(button)

    def getActiveButtonName(self):
        return self._activeButton.GetLabel()

    def setActiveButtonByName(self, name):
        self.setActiveButton(self.buttonDict[name])

    def setActiveButton(self, button):
        if button == self._activeButton:
            button.SetValue(True)
        else:
            self._activeButton.SetValue(False)
            self._activeButton = button
            self.callHandler(self.getActiveButtonName())

