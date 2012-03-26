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

class header_parser(object):
  def __init__(self, library_name):
    self.library_name = library_name
    self.extension_prefix = self.library_name.upper() + '_'
    self.constant_prefix = self.library_name.upper() + '_'
    self.function_prefix = self.library_name

  def parse(self, file_name):
    errors = []
    constants = []
    functions = []

    patterns = {}
    patterns['constant'] = r'^#define (?P<name>\w+)\s+(?P<value>[-()\w]+)$'
    patterns['function'] = r'^(?:GLAPI|extern)\s+(?P<return>\w+(?:\s*\*)?)\s+(?P<api>\w+)?\s*(?P<name>\w+)\s*\(\s*(?:void|(?P<parameters>.*))\s*\);$'
    patterns['extension'] = r'^#ifndef\s+(?P<name>\w+)$'
    patterns['reuse'] = '^/\*\s*reuse\s+(?P<name>\w+)\s*\*/$'
    patterns['reuse-tokens'] = '^/\* Reuse tokens.*$'
    patterns['enum'] = r'^/?\*\s*(?P<name>[ \w]*\w)\s*(?:\*/)?$'

    patterns['typedef-function'] = r'^typedef\s+[*\s\w]+\s*\([*\s\w]+\)\s*\(.*\);$'
    patterns['ifdef-prototypes'] = r'^(?:#ifdef|#endif /\*)\s+\w+_PROTOTYPES\s*(?:\*/)?$'
    patterns['endif'] = r'^#endif$'

    with open(file_name, 'r') as dotspec_file:
      s = stack(self.library_name, file_name, self.extension_prefix, self.extension_prefix)
      deprecated = False

      for line in [ l.strip() for l in dotspec_file if len(l.strip()) > 0 ]:
        for k, regex in patterns.items():
          match = re.match(regex, line)
          if match:
            if k == 'constant':
              constant_name = match.group('name')
              constant_value = match.group('value')

              if constant_name == s.extension_name:
                break
              elif 'WIN32_LEAN_AND_MEAN' in constant_name:
                break
              elif 'EXT_VERSION' in constant_name:
                break
              elif 'GLAPI' in constant_name:
                break
              elif 'APIENTRY' in constant_name:
                break

              if 'HISTOGRAM_GREEN_SIZE' in constant_name:
                print s.file_name, s.library_name, s.extension_name, s.category_name

              if not constant_name.startswith(self.constant_prefix):
                constant_name = self.constant_prefix + constant_name

              constants.append({'name': constant_name, 'value': constant_value, 'stack': copy(s), 'deprecated': copy(deprecated) })

            elif k == 'extension':
              extension_name = match.group('name')
              if extension_name.startswith('__'):
                break
              elif extension_name.endswith('_H'):
                break
              elif 'WIN32_LEAN_AND_MEAN' in extension_name:
                break
              elif 'GLAPI' in extension_name:
                break
              elif 'APIENTRY' in extension_name:
                break

              if not extension_name.startswith(self.extension_prefix):
                extension_name = self.extension_prefix + extension_name

              if '_DEPRECATED' in extension_name:
                deprecated = True
                extension_name = extension_name.replace('_DEPRECATED', '')
              else:
                deprecated = False

              s.extension_name = extension_name
              s.category_name = extension_name

            elif k == 'function':
              function_name = match.group('name')
              if not function_name.startswith(self.function_prefix):
                function_name = self.function_prefix + function_name

              parameters = match.group('parameters')
              param_list = []
              params = {}
              if parameters is not None:
                parameters = [ n.strip() for n in parameters.split(',') if len(n.strip()) > 0 ]
                for p in parameters:
                  param_match = re.match(r'^\s*(?P<type>[*\s\w]+)\s*(?P<name>\w+)\s*$', p)
                  if param_match:
                    param_name = param_match.group('name')
                    param_type = param_match.group('type')
                    param_list.append(param_name)

                    if '*' in param_type:
                      param_direction = 'out'
                    else:
                      param_direction = 'in'

                    params[param_name] = {'name': param_name, 'type': param_type, 'direction': param_direction}
                  else:
                    log.info(p)

              s.function_name = function_name

              functions.append({
                'parameters': dict(params),
                'parameter_list': list(param_list),
                'return': match.group('return'),
                'name': function_name,
                'stack': copy(s)
              })

            elif k == 'enum':
              enum_name = match.group('name')

              if 'Reuse tokens' in enum_name:
                break
              elif 'reuse' in enum_name:
                continue

              if not enum_name.startswith(self.extension_prefix):
                enum_name = self.extension_prefix + enum_name

              if '_DEPRECATED' in enum_name:
                deprecated = True
                enum_name = enum_name.replace('_DEPRECATED', '')
              else:
                deprecated = False

              s.category_name = enum_name

            elif k == 'reuse':
              constant_name = match.group('name')

              if not constant_name.startswith(self.constant_prefix):
                constant_name = self.constant_prefix + constant_name

              constants.append({'name': constant_name, 'value': constant_name, 'stack': copy(s), 'deprecated': copy(deprecated) })

#            elif k == 'use':
#              foreign_enum_name = match.group('enum')
#              constant_name = match.group('constant')
#
#              if not foreign_enum_name.startswith(self.extension_prefix):
#                foreign_enum_name = self.extension_prefix + foreign_enum_name
#              if not constant_name.startswith(self.constant_prefix):
#                constant_name = self.constant_prefix + constant_name
#
#              value_key = foreign_enum_name + '.' + constant_name
#              for name in s.values():
#                values[name + '.' + constant_name] = value_key
#
#              constants.append({'name': constant_name, 'value_key': value_key, 'stack': copy(s) })

            break
        else:
          errors.append('U: ' + line)

    for e in errors:
      log.error(file_name + ': ' + e)

    for c in constants:
      raw_constant(c['name'], c['value'], c['stack'])

    for f in functions:
      raw_function(f['name'], f['return'], f['parameter_list'], f['stack'])
      for k, p in f['parameters'].items():
        raw_parameter(p['name'], p['type'], p['direction'], f['stack'])
#
#    for c in constants:
#      c['value'] = values.get(c['value_key'], values.get(c['value_key'].replace('.', '_DEPRECATED.'), c['value_key']))
#
#    return [ raw_constant(c['name'], c['value'], c['stack']) for c in constants ]

class header_function_parser(object):
  def __init__(self, library_name):
    self.library_name = library_name
    self.extension_prefix = self.library_name.upper() + '_'
    self.function_prefix = self.library_name

  def parse(self, file_name):
    errors = []

    patterns = {}
    patterns['function'] = r'^extern\s+(?P<return>\w+)\s+(?P<api>\w+)?\s+(?P<name>\w+)\s*\(.*\);$'

#    patterns['comment'] = r'^#.*$'

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

            elif k == 'function':
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
