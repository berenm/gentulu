#!/usr/bin/python
# -*- coding: utf-8 -*-

# Distributed under the Boost Software License, Version 1.0.
# See accompanying file LICENSE or copy at http://www.boost.org/LICENSE

all_parameters = []

class parameter:
  def __init__(self, name, type_name, direction, stack, **kwargs):
    self.name = name
    self.type_name = type_name
    self.direction = direction

    self.stack = stack

    self.other = {}
    for k in kwargs:
      self.other[k] = kwargs[k]

    all_parameters.append(self)
