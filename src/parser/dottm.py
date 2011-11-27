#!/usr/bin/python
# -*- coding: utf-8 -*-

# Distributed under the Boost Software License, Version 1.0.
# See accompanying file LICENSE or copy at http://www.boost.org/LICENSE

import re
from utils import log

class dottm_parser(object):
  def __init__(self, library_name):
    self.library_name = library_name
    self.extension_prefix = self.library_name.upper() + '_'
    self.constant_prefix = self.library_name.upper() + '_'

  def parse(self, file_name):
    errors = []

    mappings = {}

    patterns = {}
    patterns['type'] = r'^(?P<name>\w+),\*,\*,\s*(?P<type>(?:struct |unsigned |const )?[*\w]+(?: \*| const)?),\*,\*,?$'
    patterns['comment'] = r'^#.*$'

    with open(file_name, 'r') as dottm_file:
      for line in [ l.strip() for l in dottm_file if len(l.strip()) > 0 ]:
        for k, regex in patterns.items():
          match = re.match(regex, line)
          if match:
            if k == 'type':
              type_name = match.group('type')
              if type == '*':
                type_name = match.group('name')

              mappings[match.group('name')] = type_name

            break
        else:
          errors.append('U: ' + line)

    for e in errors:
      log.error(file_name + ': ' + e)

    return mappings
