#!/usr/bin/python
# -*- coding: utf-8 -*-

# Distributed under the Boost Software License, Version 1.0.
# See accompanying file LICENSE or copy at http://www.boost.org/LICENSE

libraries = {}

class category:
  def __init__(self, name):
    self.name = name
    self.functions = {}
    self.constants = {}


class categories(dict):
  def __init__(self, extension_name, group_name, library_name):
    self.extension_name = extension_name
    self.group_name = group_name
    self.library_name = library_name

  def __getitem__(self, category_name):
    if category_name.upper().startswith(self.library_name.upper()):
      category_name = category_name[len(self.library_name):]
    category_name = category_name.strip('_')
    if category_name.upper().startswith(self.group_name.upper()):
      category_name = category_name[len(self.group_name):]
    category_name = category_name.strip('_')
    if category_name.upper().startswith(self.extension_name.upper()):
      category_name = category_name[len(self.extension_name):]
    category_name = category_name.strip('_')

    if not category_name in self:
      self[category_name] = category(category_name)
    return dict.__getitem__(self, category_name)

class extension:
  def __init__(self, name, group_name, library_name):
    self.name = name
    self.categories = categories(self.name, group_name, library_name)


class extensions(dict):
  def __init__(self, group_name, library_name):
    self.group_name = group_name
    self.library_name = library_name

  def __getitem__(self, extension_name):
    if extension_name.upper().startswith(self.library_name.upper()):
      extension_name = extension_name[len(self.library_name):]
    extension_name = extension_name.strip('_')
    if extension_name.upper().startswith(self.group_name.upper()):
      extension_name = extension_name[len(self.group_name):]
    extension_name = extension_name.strip('_')

    if not extension_name in self:
      self[extension_name] = extension(extension_name, self.group_name, self.library_name)
    return dict.__getitem__(self, extension_name)

class group:
  def __init__(self, name, library_name):
    self.name = name
    self.extensions = extensions(self.name, library_name)


class groups(dict):
  def __init__(self, library_name):
    self.library_name = library_name

  def get_group_name(self, extension_name):
    if extension_name.upper().startswith(self.library_name.upper()):
      extension_name = extension_name[len(self.library_name):]
    extension_name = extension_name.strip('_')

    if not '_' in extension_name:
      return self.library_name.upper()
    else:
      return extension_name.split('_')[0]

  def __getitem__(self, extension_name):
    group_name = self.get_group_name(extension_name)

    if not group_name in self:
      self[group_name] = group(group_name, self.library_name)
    return dict.__getitem__(self, group_name)

class library:
  def __init__(self, name):
    self.name = name
    self.groups = groups(self.name)

  @staticmethod
  def get(name):
    if name not in libraries:
      libraries[name] = library(name)

    return libraries[name]

def print_tree(printer, category_action):
  printer.begin()
  for li in libraries.values():
    printer.begin_library(li)
    for gr in li.groups.values():
      printer.begin_group(gr)
      for ex in gr.extensions.values():
        printer.begin_extension(ex)
        for ca in ex.categories.values():
          printer.begin_category(ca)
          category_action(ca, printer)
          printer.end_category(ca)
        printer.end_extension(ex)
      printer.end_group(gr)
    printer.end_library(li)
  printer.end()
