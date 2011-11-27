#!/usr/bin/python
# -*- coding: utf-8 -*-

# Distributed under the Boost Software License, Version 1.0.
# See accompanying file LICENSE or copy at http://www.boost.org/LICENSE

import re
from utils import log
from object.constant import raw_constant
from object.function import raw_function
from object.parameter import raw_parameter
from object.stack import stack
from copy import copy

class dotspec_constant_parser(object):
  def __init__(self, library_name):
    self.library_name = library_name
    self.extension_prefix = self.library_name.upper() + '_'
    self.constant_prefix = self.library_name.upper() + '_'

  def parse(self, file_name):
    errors = []
    values = {}
    constants = []

    patterns = {}
    patterns['raw_constant'] = r'^(?P<name>\w+)\s*=\s*(?P<value>[-()\w]+)(?:\s*#.*)?$'
    patterns['extension'] = r'^(?P<name>\w+)\s*enum\s*:\s*(?P<comments>.*)$'
    patterns['enum'] = r'^passthru:\s*/\*\s*(?P<name>\w+)\s*\*/$'
    patterns['use'] = r'^use\s(?P<enum>\w+)\s*(?P<raw_constant>\w+)$'

    patterns['comment'] = r'^#.*$'
    patterns['passthru-reuse'] = r'^passthru.*Reuse.*$'

    with open(file_name, 'r') as dotspec_file:
      s = stack(self.library_name, file_name, self.extension_prefix, self.extension_prefix)

      for line in [ l.strip() for l in dotspec_file if len(l.strip()) > 0 ]:
        for k, regex in patterns.items():
          match = re.match(regex, line)
          if match:
            if k == 'raw_constant':
              constant_name = match.group('name')
              constant_value = match.group('value')

              if not constant_name.startswith(self.constant_prefix):
                constant_name = self.constant_prefix + constant_name

              if constant_value.startswith(self.constant_prefix):
                constant_value = self.library_name + '.' + constant_value

              value_key = s.category_name + '.' + constant_name
              for name in s.values():
                values[name + '.' + constant_name] = constant_value

              constants.append({'name': constant_name, 'value_key': value_key, 'stack': copy(s) })

            elif k == 'extension':
              extension_name = match.group('name')
              if not extension_name.startswith(self.extension_prefix):
                extension_name = self.extension_prefix + extension_name

              s.extension_name = extension_name
              s.category_name = extension_name

            elif k == 'enum':
              enum_name = match.group('name')
              if not enum_name.startswith(self.extension_prefix):
                enum_name = self.extension_prefix + enum_name

              s.category_name = enum_name

            elif k == 'use':
              foreign_enum_name = match.group('enum')
              constant_name = match.group('raw_constant')

              if not foreign_enum_name.startswith(self.extension_prefix):
                foreign_enum_name = self.extension_prefix + foreign_enum_name
              if not constant_name.startswith(self.constant_prefix):
                constant_name = self.constant_prefix + constant_name

              value_key = foreign_enum_name + '.' + constant_name
              for name in s.values():
                values[name + '.' + constant_name] = value_key

              constants.append({'name': constant_name, 'value_key': value_key, 'stack': copy(s) })

            break
        else:
          errors.append('U: ' + line)

    for e in errors:
      log.error(file_name + ': ' + e)

    for k, v in values.items():
      while v.startswith(self.extension_prefix) or v.startswith(self.constant_prefix) or v.startswith(self.library_name):
        if not '.' in v:
          v = self.extension_prefix + '.' + v

        values[k] = values.get(v, values.get(v.replace('.', '_DEPRECATED.'), v))
        v = values[k]

    for c in constants:
      c['value'] = values.get(c['value_key'], values.get(c['value_key'].replace('.', '_DEPRECATED.'), c['value_key']))

    return [ raw_constant(c['name'], c['value'], c['stack']) for c in constants ]

class dotspec_function_parser(object):
  def __init__(self, library_name):
    self.library_name = library_name
    self.extension_prefix = self.library_name.upper() + '_'
    self.function_prefix = self.library_name

  def parse(self, file_name):
    errors = []

    patterns = {}
    patterns['param'] = r'^param\s+(?P<name>\w+)\s+(?P<type>\w+)\s+(?P<direction>\w+)\s+(?P<underlying_type>\w+)\s*(?P<cardinality>\[[\(\)*,/\w]*\])?\s*(?P<retained>retained)?$'
    patterns['return'] = r'^return\s+(?P<type>\w+)$'
    patterns['category'] = r'^category\s+(?P<name>\w+)(?:\s*# old:\s*(?P<old>[-\w]+))?$'
    patterns['subcategory'] = r'^subcategory\s+(?P<name>\w+)$'
    patterns['raw_function'] = r'^(?P<name>\w+)\s*\((?P<parameters>[\w\s,]*)\)$'
    patterns['version'] = r'^version\s+(?P<version>[.\w]+)$'
    patterns['deprecated'] = r'^deprecated\s+(?P<deprecated>[.\w]+)$'
    patterns['vectorequiv'] = r'^vectorequiv\s+(?P<name>[.\w]+)$'
    patterns['alias'] = r'^alias\s+(?P<alias>[.\w]+)$'

    patterns['categories'] = r'^category:\s+(?P<names>[-\s\w]+)$'
    patterns['newcategory'] = r'^newcategory:\s+(?P<name>[-\w]+)$'

    patterns['comment'] = r'^#.*$'
    patterns['passthru'] = r'^passthru.*$'
    patterns['glxflags'] = r'^glxflags.*$'
    patterns['glxvendorglx'] = r'^glxvendorglx.*$'
    patterns['glxvendorpriv'] = r'^glxvendorpriv.*$'
    patterns['glxopcode'] = r'^glxopcode.*$'
    patterns['glxropcode'] = r'^glxropcode.*$'
    patterns['glxsingle'] = r'^glxsingle.*$'
    patterns['dlflags'] = r'^dlflags.*$'
    patterns['offset'] = r'^offset.*$'
    patterns['glfflags'] = r'^glfflags.*$'
    patterns['beginend'] = r'^beginend.*$'
    patterns['wglflags'] = r'^wglflags.*$'
    patterns['extension'] = r'^extension.*$'
    patterns['glextmask'] = r'^glextmask.*$'
    patterns['glxvectorequiv'] = r'^glxvectorequiv.*$'

    functions = []
    current_function = None

    with open(file_name, 'r') as dotspec_file:
      s = stack(self.library_name, file_name, self.extension_prefix, self.extension_prefix)

      for line in [ l.strip() for l in dotspec_file if len(l.strip()) > 0 ]:
        for k, regex in patterns.items():
          match = re.match(regex, line)
          if match:
            if k == 'param':
              current_param = current_function['parameters'][match.group('name')]
              current_param['name'] = match.group('name')
              current_param['type'] = match.group('type')
              current_param['direction'] = match.group('direction')
              current_param['underlying_type'] = match.group('underlying_type')

              current_param['cardinality'] = match.group('cardinality')

            elif k == 'vectorequiv':
              current_function['vectorequiv'] = match.group('name')

            elif k == 'alias':
              current_function['alias'] = match.group('alias')

            elif k == 'return':
              current_function['return'] = match.group('type')

            elif k == 'version':
              current_function['version'] = match.group('version')

            elif k == 'deprecated':
              current_function['deprecated'] = match.group('deprecated')

            elif k == 'subcategory':
              category_name = match.group('name')
              if not category_name.startswith(self.extension_prefix):
                category_name = self.extension_prefix + category_name

              s.category_name = category_name

            elif k == 'category':
              extension_name = match.group('name')
              if not extension_name.startswith(self.extension_prefix):
                extension_name = self.extension_prefix + extension_name

              category_name = match.group('old')
              if category_name is None:
                category_name = extension_name
              if not category_name.startswith(self.extension_prefix):
                category_name = self.extension_prefix + category_name

              s.extension_name = extension_name
              s.category_name = category_name

            elif k == 'raw_function':
              if current_function is not None:
                functions.append(current_function)

              function_name = match.group('name')
              if not function_name.startswith(self.function_prefix):
                function_name = self.function_prefix + function_name

              s = copy(s)
              parameters = [ n.strip() for n in match.group('parameters').split(',') if len(n.strip()) > 0 ]
              current_function = {
                'parameters': dict([ (n.strip(), {}) for n in parameters ]),
                'parameter_list': parameters,
                'name': function_name,
                'stack': s
              }
              s.function_name = function_name

            break
        else:
          errors.append('U: ' + line)

    for e in errors:
      log.error(file_name + ': ' + e)

    for f in functions:
      raw_function(f['name'], f['return'], f['parameter_list'], f['stack'])
      for k, p in f['parameters'].items():
        raw_parameter(p['name'], p['type'], p['direction'], f['stack'], cardinality=p['cardinality'], underlying_type=p['underlying_type'])
