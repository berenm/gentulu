#!/usr/bin/python
# -*- coding: utf-8 -*-

# Distributed under the Boost Software License, Version 1.0.
# See accompanying file LICENSE or copy at http://www.boost.org/LICENSE

import re
from object.constant import constant
from object.enum import enum, unknown_enum
from utils import log

class dotspec_parser(object):
  def __init__(self, library_name):
    self.library_name = library_name
    self.enum_prefix = self.library_name.upper() + '_'
    self.constant_prefix = self.library_name.upper() + '_'
    self.function_prefix = self.library_name.lower()

  def parse(self, filename):
    errors = []
    values = {}
    constants = []

    with open(filename, 'r') as dotspec_file:
      current_enum = unknown_enum

      for line in dotspec_file:
        line = line.split('#')[0].strip()
        if len(line) == 0:
          continue

        if '=' in line:
          match = re.match('^(?P<name>\w+)\s*=\s*(?P<value>(?:-|\w)+)', line)
          if match:
            enum_name = current_enum.name
            constant_name = match.group('name')
            constant_value = match.group('value')
            if not constant_name.startswith(self.constant_prefix):
              constant_name = self.constant_prefix + constant_name

            values[enum_name + '.' + constant_name] = constant_value
            constants.append({'enum_name': enum_name, 'name': constant_name, 'value_key': enum_name + '.' + constant_name })
          else:
            errors.append('U(=): ' + line)

        elif 'passthru:' in line:
          continue

        elif ':' in line:
          match = re.match('^(?P<name>\w+)\s*enum\s*:\s*(?P<comments>.*)\s*$', line)
          if match:
            enum_name = match.group('name')
            if not enum_name.startswith(self.enum_prefix):
              enum_name = self.enum_prefix + enum_name

            current_enum = enum(enum_name, comments=match.group('comments'))
          else:
            errors.append('U(:): ' + line)

        elif 'use' == line[0:3]:
          match = re.match('^use\s(?P<enum>\w+)\s*(?P<constant>\w+)\s*$', line)
          if match:
            enum_name = match.group('enum')
            constant_name = match.group('constant')

            if not enum_name.startswith(self.enum_prefix):
              enum_name = self.enum_prefix + enum_name
            if not constant_name.startswith(self.constant_prefix):
              constant_name = self.constant_prefix + constant_name

            constants.append({'enum_name': current_enum.name, 'name': constant_name, 'value_key': enum_name + '.' + constant_name })
          else:
            errors.append('U(use): ' + line)

        else:
          errors.append('U: ' + line)

    for c in constants:
      constant(c['name'], values.get(c['value_key'], values.get(c['value_key'].replace('.', '_DEPRECATED.'), c['value_key'])), c['enum_name'])

    for e in errors:
      log.error(filename + ': ' + e)
