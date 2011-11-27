#!/usr/bin/python
# -*- coding: utf-8 -*-

# Distributed under the Boost Software License, Version 1.0.
# See accompanying file LICENSE or copy at http://www.boost.org/LICENSE

raw_functions = []

class raw_function:
  def __init__(self, name, return_type, parameters, stack, **kwargs):
    self.name = name
    self.return_type = return_type
    self.parameters = parameters

    self.stack = stack

    self.other = {}
    for k in kwargs:
      self.other[k] = kwargs[k]

    raw_functions.append(self)
