#!/usr/bin/python
# -*- coding: utf-8 -*-

# Distributed under the Boost Software License, Version 1.0.
# See accompanying file LICENSE or copy at http://www.boost.org/LICENSE

from printer import printer_base
import re

class cpp_printer(printer_base):

  def begin_namespace(self, o):
    if o.name is not None and len(o.name.strip()) > 0:
      self.scope_name = o.name.lower()
      self.scope_name = re.sub(r'^(?P<n>[0-9])', r'_\g<n>', self.scope_name)
      self.scope_name = self.scope_name.replace('-', '_')
      print 'namespace %s {' % self.scope_name

  def end_namespace(self, o):
    if o.name is not None and len(o.name.strip()) > 0:
      self.scope_name = o.name.lower()
      self.scope_name = re.sub(r'^(?P<n>[0-9])', r'_\g<n>', self.scope_name)
      self.scope_name = self.scope_name.replace('-', '_')
      print '} // namespace %s' % self.scope_name

  def begin_library(self, li):
    self.begin_namespace(li)
  def end_library(self, li):
    self.end_namespace(li)

  def begin_group(self, gr):
    self.begin_namespace(gr)
  def end_group(self, gr):
    self.end_namespace(gr)

  def begin_extension(self, ex):
    self.begin_namespace(ex)
  def end_extension(self, ex):
    self.end_namespace(ex)

  def begin_constants(self, ca):
    if len(ca.constants) > 0:
      print 'enum constants {'
  def end_constants(self, ca):
    if len(ca.constants) > 0:
      print '};'

  def begin_constant(self, c):
    print '    ', c.name, '=', c.value + ','

  def serialize_parameter(self, p):
    if p.other['underlying_type'] == 'array':
      return '%s* %s /* %s, card: %s */' % (p.type_name, p.name, p.direction, p.other['cardinality'])
    else:
      if p.other['cardinality'] is not None:
        return '%s %s /* %s, !card: %s */' % (p.type_name, p.name, p.direction, p.other['cardinality'])
      else:
        return '%s %s /* %s */' % (p.type_name, p.name, p.direction)

  def begin_function(self, f):
    print '    ', f.name, '(', ', '.join([ self.serialize_parameter(f.parameters[p]) for p in f.parameter_list ]), ');'
  def end_function(self, f):
    pass
