#!/usr/bin/python
# -*- coding: utf-8 -*-

# Distributed under the Boost Software License, Version 1.0.
# See accompanying file LICENSE or copy at http://www.boost.org/LICENSE

class printer_base:
  def begin(self):
    pass
  def end(self):
    pass

  def begin_library(self, li):
    pass
  def end_library(self, li):
    pass

  def begin_group(self, gr):
    pass
  def end_group(self, gr):
    pass

  def begin_extension(self, ex):
    pass
  def end_extension(self, ex):
    pass

  def begin_category(self, ca):
    pass
  def end_category(self, ca):
    pass

  def begin_constants(self, ca):
    pass
  def end_constants(self, ca):
    pass

  def begin_constant(self, c):
    pass
  def end_constant(self, c):
    pass

  def begin_functions(self, ca):
    pass
  def end_functions(self, ca):
    pass

  def begin_function(self, f):
    pass
  def end_function(self, f):
    pass
