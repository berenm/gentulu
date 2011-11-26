#!/usr/bin/python
# -*- coding: utf-8 -*-

# Distributed under the Boost Software License, Version 1.0.
# See accompanying file LICENSE or copy at http://www.boost.org/LICENSE

constants = []

class constant():
  def __init__(self, name, value, enum_name):
    self.name = name
    self.value = value
    self.enum_name = enum_name

    constants.append(self)
