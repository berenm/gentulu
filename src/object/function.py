#!/usr/bin/python
# -*- coding: utf-8 -*-

# Distributed under the Boost Software License, Version 1.0.
# See accompanying file LICENSE or copy at http://www.boost.org/LICENSE

from object.library import library, print_tree
from object.parameter import reduce_parameters
from utils import log

raw_functions = []

class raw_function:
  def __init__(self, name, return_type, parameter_list, stack, **kwargs):
    self.name = name
    self.return_type = return_type
    self.parameter_list = parameter_list
    self.parameters = {}

    self.stack = stack

    self.other = {}
    for k in kwargs:
      self.other[k] = kwargs[k]

    raw_functions.append(self)

def reduce_functions():
  for f in raw_functions:
    li = library.get(f.stack.library_name)
    gr = li.groups[f.stack.extension_name]
    ex = gr.extensions[f.stack.extension_name]
    ca = ex.categories[f.stack.category_name]

    if not f.name in ca.functions:
      ca.functions[f.name] = f
    else:
      log.warn('F %s already in %s.%s.%s' % (f.name, li.name, ex.name, ca.name))

  reduce_parameters()

def print_category_functions(category, function_printer):
  function_printer.begin_functions(category)
  for f in category.functions.values():
    function_printer.begin_function(f)
    function_printer.end_function(f)
  function_printer.end_functions(category)

def print_functions(function_printer):
  print_tree(function_printer, lambda category, printer: print_category_functions(category, printer))
