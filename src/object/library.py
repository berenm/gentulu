#!/usr/bin/python
# -*- coding: utf-8 -*-

# Distributed under the Boost Software License, Version 1.0.
# See accompanying file LICENSE or copy at http://www.boost.org/LICENSE
from module import module

class library(module):
  def __init__(self, name):
    module.__init__(self, name)

    self.type_prefix = self.name.upper()
    self.type_suffix = ''
    self.constant_prefix = self.name.upper() + '_'
    self.constant_suffix = ''
    self.function_prefix = self.name
    self.function_suffix = ''
