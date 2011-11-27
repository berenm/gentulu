#!/usr/bin/python
# -*- coding: utf-8 -*-

# Distributed under the Boost Software License, Version 1.0.
# See accompanying file LICENSE or copy at http://www.boost.org/LICENSE

raw_constants = []

class raw_constant:
  def __init__(self, name, value, stack, **kwargs):
    self.name = name
    self.value = value

    self.stack = stack

    self.other = {}
    for k in kwargs:
      self.other[k] = kwargs[k]

    raw_constants.append(self)
