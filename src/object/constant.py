#!/usr/bin/python
# -*- coding: utf-8 -*-

# Distributed under the Boost Software License, Version 1.0.
# See accompanying file LICENSE or copy at http://www.boost.org/LICENSE

constants = []

class constant:
  def __init__(self, name, value, extension_name, enum_name, **kwargs):
    self.name = name
    self.value = value

    self.extension_name = extension_name
    self.enum_name = enum_name

    constants.append(self)
