#!/usr/bin/python
# -*- coding: utf-8 -*-

# Distributed under the Boost Software License, Version 1.0.
# See accompanying file LICENSE or copy at http://www.boost.org/LICENSE

from printer import printer_base

class basic_printer(printer_base):
  def begin_library(self, li):
    print 'L:', li.name

  def begin_group(self, gr):
    print ' G:', gr.name

  def begin_extension(self, ex):
    print '  E:', ex.name

  def begin_category(self, ca):
    print '   C:', ca.name

  def begin_constant(self, c):
    print '    ', c.name, '=', c.value

  def serialize_parameter(self, p):
    return '%s %s%s <%s>' % (p.type_name, p.name, p.other['cardinality'], p.direction)
  def begin_function(self, f):
    print '    ', f.name, '(', ', '.join([ self.serialize_parameter(f.parameters[p]) for p in f.parameter_list ]), ')'
