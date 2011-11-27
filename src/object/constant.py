#!/usr/bin/python
# -*- coding: utf-8 -*-

# Distributed under the Boost Software License, Version 1.0.
# See accompanying file LICENSE or copy at http://www.boost.org/LICENSE

from object.library import library, print_tree
from utils import log

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

def reduce_constants():
  for c in raw_constants:
    li = library.get(c.stack.library_name)
    gr = li.groups[c.stack.extension_name]
    ex = gr.extensions[c.stack.extension_name]
    ca = ex.categories[c.stack.category_name]

    if not c.name in ca.constants:
      ca.constants[c.name] = c
    elif c.value != ca.constants[c.name].value:
      log.warn('C %s (%s, %s) already in %s.%s.%s' % (c.name, c.value, ca.constants[c.name].value, li.name, ex.name, ca.name))

def print_category_constants(category, constant_printer):
  constant_printer.begin_constants(category)
  for c in category.constants.values():
    constant_printer.begin_constant(c)
    constant_printer.end_constant(c)
  constant_printer.end_constants(category)

def print_constants(constant_printer):
  print_tree(constant_printer, lambda category, printer: print_category_constants(category, printer))
