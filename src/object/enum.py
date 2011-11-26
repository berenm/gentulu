#!/usr/bin/python
# -*- coding: utf-8 -*-

# Distributed under the Boost Software License, Version 1.0.
# See accompanying file LICENSE or copy at http://www.boost.org/LICENSE

enums = []

class enum():
  def __init__(self, name, **kwargs):
    self.name = name

    self.other = {}
    for k in kwargs:
      self.other[k] = kwargs[k]

    enums.append(self)

unknown_enum = enum('__gentulu_unknown_enum')

