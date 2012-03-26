#!/usr/bin/python
# -*- coding: utf-8 -*-

# Distributed under the Boost Software License, Version 1.0.
# See accompanying file LICENSE or copy at http://www.boost.org/LICENSE

from object.library import library
from utils import log

raw_parameters = []
type_mappings = {}

class raw_parameter:
  def __init__(self, name, type_name, direction, stack, **kwargs):
    self.name = name
    self.type_name = type_name
    self.direction = direction

    self.stack = stack

    self.other = {}
    for k in kwargs:
      self.other[k] = kwargs[k]

    raw_parameters.append(self)

class parameter:
  def __init__(self, raw_p):
    self.name = raw_p.name
    self.original_type_name = raw_p.type_name
    self.type_name = type_mappings.get(raw_p.type_name, raw_p.type_name)
    self.direction = raw_p.direction

    self.other = dict(raw_p.other)

def reduce_parameters():
  for p in raw_parameters:
    li = library.get(p.stack.library_name)
    gr = li.groups[p.stack.extension_name.upper()]
    ex = gr.extensions[p.stack.extension_name.lower()]
#    ca = ex.categories[p.stack.category_name.lower()]
    ca = ex.categories['functions']
    fn = ca.functions[p.stack.function_name]

    if not p.name in fn.parameters:
      fn.parameters[p.name] = parameter(p)
    else:
      log.warn('P %s already in %s.%s.%s.%s' % (p.name, li.name, ex.name, ca.name, fn.name))
