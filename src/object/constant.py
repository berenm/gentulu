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

class constant:
  def __init__(self, raw_c):
    self.name = raw_c.name
    self.value = raw_c.value

    self.other = raw_c.other

    self.in_files = set([raw_c.stack.file_name])

  def update(self, o):
    self.in_files.update(o.in_files)

    for k, v in o.other:
      if k in self.other and self.other[k] != v:
        log.warn('updating current constant %s = %s to %s' % (k, self.other[k], v))
      self.other[k] = v

  def __eq__(self, o):
    if isinstance(o, constant):
      return self.name == o.name and self.value == o.value
    return False

  def __ne__(self, o):
    return not self == o

def reduce_constants():
  log.info('resolving constant values...')
  for c in raw_constants:
    while '_' in c.value:
      if '.' in c.value:
        scope_name, constant_name = c.value.split('.')
      else:
        scope_name = None
        constant_name = c.value

      resolved_values = set([ o.value for o in raw_constants if o.name == constant_name and o.value != constant_name and scope_name in [ None, o.stack.library_name, o.stack.extension_name, o.stack.category_name ] ])
      if len(resolved_values) > 1:
        log.warn(c.name + ': ' + c.value + ', multiple value possible, taking first: ' + str(resolved_values))
        c.value = resolved_values.pop()
      elif len(resolved_values) > 0:
        c.value = resolved_values.pop()
      else:
        log.warn(c.name + ': ' + c.value + ', no value found')
        break

  log.info('reducing constants...')
  for rc in raw_constants:
    li = library.get(rc.stack.library_name)
    gr = li.groups[rc.stack.extension_name.upper()]
    ex = gr.extensions[rc.stack.extension_name.lower()]
#    ca = ex.categories[c.stack.category_name.lower()]
    ca = ex.categories['constants']

    c = constant(rc)
    if not c.name in ca.constants:
      ca.constants[c.name] = constant(c)
    elif c == ca.constants[c.name]:
      ca.constants[c.name].update(c)
    else:
      log.warn('C %s (%s, %s) already in %s.%s.%s' % (c.name, c.value, ca.constants[c.name].value, li.name, ex.name, ca.name))
    else:

def print_category_constants(category, constant_printer):
  constant_printer.begin_constants(category)
  for c in category.constants.values():
    constant_printer.begin_constant(c)
    constant_printer.end_constant(c)
  constant_printer.end_constants(category)

def print_constants(constant_printer):
  print_tree(constant_printer, lambda category, printer: print_category_constants(category, printer))
