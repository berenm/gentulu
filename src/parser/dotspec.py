#!/usr/bin/python
# -*- coding: utf-8 -*-

# Distributed under the Boost Software License, Version 1.0.
# See accompanying file LICENSE or copy at http://www.boost.org/LICENSE

import re
from utils import log

class dotspec_enum_parser(object):
  def __init__(self, library_name):
    self.library_name = library_name
    self.module_prefix = self.library_name.upper() + '_'
    self.enum_prefix = self.library_name.upper() + '_'
    self.constant_prefix = self.library_name.upper() + '_'
    self.function_prefix = self.library_name

  def parse(self, filename):
    errors = []
    values = {}
    constants = []

    patterns = {}
    patterns['constant'] = r'^^(?P<name>\w+)\s*=\s*(?P<value>[-()\w]+)(?:\s*#.*)?$'
    patterns['enum'] = r'^(?P<name>\w+)\s*enum\s*:\s*(?P<comments>.*)$'
    patterns['sub-enum'] = r'^passthru:\s*/\*\s*(?P<name>\w+)\s*\*/$'
    patterns['use'] = r'^use\s(?P<enum>\w+)\s*(?P<constant>\w+)$'

    patterns['comment'] = r'^#.*$'
    patterns['passthru-reuse'] = r'^passthru.*Reuse.*$'

    enums = []

    with open(filename, 'r') as dotspec_file:
      enum_stack = [ self.enum_prefix, self.enum_prefix, self.enum_prefix ]

      for line in [ l.strip() for l in dotspec_file if len(l.strip()) > 0 ]:
        matched = False
        for k, regex in patterns.items():
          match = re.match(regex, line)
          if match:
            matched = True

            if k == 'constant':
              current_enum = enum_stack[-1]
              constant_name = match.group('name')
              constant_value = match.group('value')

              if not constant_name.startswith(self.constant_prefix):
                constant_name = self.constant_prefix + constant_name

              value_key = current_enum + '.' + constant_name
              for e in enum_stack:
                values[e + '.' + constant_name] = constant_value

              constants.append({'enum_name': current_enum, 'name': constant_name, 'value_key': value_key })

            elif k == 'enum':
              enum_name = match.group('name')
              if not enum_name.startswith(self.enum_prefix):
                enum_name = self.enum_prefix + enum_name

              enums.append(enum_name)

              enum_stack.pop()
              enum_stack.pop()
              enum_stack.append(enum_name)
              enum_stack.append(enum_name)

            elif k == 'sub-enum':
              enum_name = match.group('name')
              if not enum_name.startswith(self.enum_prefix):
                enum_name = self.enum_prefix + enum_name

              enums.append(enum_name)

              enum_stack.pop()
              enum_stack.append(enum_name)

            elif k == 'use':
              current_enum = enum_stack[-1]
              enum_name = match.group('enum')
              constant_name = match.group('constant')

              if not enum_name.startswith(self.enum_prefix):
                enum_name = self.enum_prefix + enum_name
              if not constant_name.startswith(self.constant_prefix):
                constant_name = self.constant_prefix + constant_name

              value_key = enum_name + '.' + constant_name

              for e in enum_stack:
                values[e + '.' + constant_name] = value_key

              constants.append({'enum_name': current_enum, 'name': constant_name, 'value_key': value_key })

            break

        if not matched:
          errors.append('U: ' + line)

    for e in errors:
      log.error(filename + ': ' + e)

    for k, v in values.items():
      while v.startswith(self.enum_prefix) or v.startswith(self.constant_prefix):
        if not '.' in v:
          v = self.enum_prefix + '.' + v

        values[k] = values.get(v, values.get(v.replace('.', '_DEPRECATED.'), v))
        v = values[k]

    for c in constants:
      c['value'] = values.get(c['value_key'], values.get(c['value_key'].replace('.', '_DEPRECATED.'), c['value_key']))

class dotspec_function_parser(object):
  def __init__(self, library_name):
    self.library_name = library_name
    self.module_prefix = self.library_name.upper() + '_'
    self.enum_prefix = self.library_name.upper() + '_'
    self.constant_prefix = self.library_name.upper() + '_'
    self.function_prefix = self.library_name

  def parse(self, filename):
    errors = []

    patterns = {}
    patterns['param'] = r'^param\s+(?P<name>\w+)\s+(?P<type>\w+)\s+(?P<direction>\w+)\s+(?P<class>\w+)\s*(?P<cardinality>\[[\(\)*,/\w]*\])?\s*(?P<retained>retained)?$'
    patterns['return'] = r'^return\s+(?P<type>\w+)$'
    patterns['category'] = r'^category\s+(?P<name>\w+)(?:\s*# old:\s*(?P<old>[-\w]+))?$'
    patterns['subcategory'] = r'^subcategory\s+(?P<name>\w+)$'
    patterns['function'] = r'^(?P<name>\w+)\s*\((?P<parameters>[\w\s,]*)\)$'
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

    known_categories = []
    categories = {}

    functions = []
    current_function = None

    with open(filename, 'r') as dotspec_file:
      for line in [ l.strip() for l in dotspec_file if len(l.strip()) > 0 ]:
        matched = False
        for k, regex in patterns.items():
          match = re.match(regex, line)
          if match:
            matched = True

            if k == 'param':
              current_param = current_function['parameters'][match.group('name')]
              current_param['name'] = match.group('name')
              current_param['type'] = match.group('type')
              current_param['direction'] = match.group('direction')
              current_param['class'] = match.group('class')
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
              submodule_name = match.group('name')
              if not submodule_name.startswith(self.module_prefix):
                submodule_name = self.module_prefix + submodule_name

              current_function['sub-module'] = submodule_name

            elif k == 'category':
              module_name = match.group('name')
              if not module_name.startswith(self.module_prefix):
                module_name = self.module_prefix + module_name

              submodule_name = match.group('old')
              if submodule_name and not submodule_name.startswith(self.module_prefix):
                submodule_name = self.module_prefix + submodule_name

              current_function['module'] = module_name
              current_function['submodule'] = submodule_name

            elif k == 'function':
              if current_function is not None:
                functions.append(current_function)

              function_name = match.group('name')
              if not function_name.startswith(self.function_prefix):
                function_name = self.function_prefix + function_name

              current_function = {
                'parameters': dict([ (n.strip(), {}) for n in match.group('parameters').split(',') ]),
                'parameter_list': [ n.strip() for n in match.group('parameters').split(',') ],
                'name': function_name
              }

            break

        if not matched:
          errors.append('U: ' + line)

#      for f in functions:
#        print f['name'], f.get('module', '<none>'), f.get('sub-module', '<none>')
#        else:
#          errors.append('U: ' + line)

    for e in errors:
      log.error(filename + ': ' + e)
