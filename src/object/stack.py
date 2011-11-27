#!/usr/bin/python
# -*- coding: utf-8 -*-

# Distributed under the Boost Software License, Version 1.0.
# See accompanying file LICENSE or copy at http://www.boost.org/LICENSE

class stack:
  def __init__(self, library_name, file_name, extension_name, category_name, function_name=None):
    self.library_name = library_name
    self.file_name = file_name
    self.extension_name = extension_name
    self.category_name = category_name
    self.function_name = function_name

  def values(self):
    return [ n for n in [ self.library_name, self.file_name, self.extension_name, self.category_name, self.function_name ] if n is not None ]
