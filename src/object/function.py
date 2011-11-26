#!/usr/bin/python
# -*- coding: utf-8 -*-

# Distributed under the Boost Software License, Version 1.0.
# See accompanying file LICENSE or copy at http://www.boost.org/LICENSE

constants = []

class function:
  def __init__(self, name, return_type, extension_name, category_name, **kwargs):
    self.name = name
    self.return_type = return_type

    self.extension_name = extension_name
    self.category_name = category_name

    if self.extension_name is None:
      print self.name, self.return_type

    constants.append(self)
