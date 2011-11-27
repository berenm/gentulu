#!/usr/bin/python
# -*- coding: utf-8 -*-

# Distributed under the Boost Software License, Version 1.0.
# See accompanying file LICENSE or copy at http://www.boost.org/LICENSE

from lxml import etree, html
from resolver import resolver
import re
from parser.docbook import docbook_parser
from parser.extension import extension_parser
from parser.dotspec import dotspec_constant_parser, dotspec_function_parser
from parser.dottm import dottm_parser
from utils import log, option_parser, print_help
from object.constant import raw_constants
from object.function import raw_functions
from object.library import library, libraries

parser = option_parser()
(o, a) = parser.parse_args()

# Registering the Resolver as the default DTD Resolver
xml_parser = etree.XMLParser(load_dtd=True)
xml_parser.resolvers.add(resolver())
etree.set_default_parser(xml_parser)

class source(object):
  def __init__(self, library_name, parser, **kwargs):
    self.library_name = library_name
    self.parser = parser(self.library_name)
    self.files = []

    if 'index' in kwargs:
      local_file = resolver.cache(kwargs['index'])
      root = html.parse(local_file)
      uris = root.xpath(kwargs['xpath'])

      self.files.extend([ kwargs['base'] + f for f in filter(lambda x : re.match(kwargs['regexp'], x), uris) ])
      self.files.sort()
    else:
      self.files = kwargs['files']

    for f in self.files:
      log.debug(self.library_name + ': ' + f)

  def parse(self):
    for url in self.files:
      local_file = resolver.cache(url)
      self.parser.parse(local_file)

sources = []

# 'base' and 'index' shoud be the same in 99% of cases,
# but it's faster to download .xml on http rather than webdav over https
#sources.append(source('gl2', docbook_parser(),
#    regexp=r'^gl[A-Z][a-zA-Z0-9]*\.xml$',
#    xpath='//file/@name',
#    index='https://cvs.khronos.org/svn/repos/ogl/trunk/ecosystem/public/sdk/docs/man/',
#    base='http://www.opengl.org/sdk/docs/man/'))
#
#sources.append(source('gl3', docbook_parser(),
#    regexp=r'^gl[A-Z][a-zA-Z0-9]*\.xml$',
#    xpath='//file/@name',
#    index='https://cvs.khronos.org/svn/repos/ogl/trunk/ecosystem/public/sdk/docs/man3/',
#    base='http://www.opengl.org/sdk/docs/man3/'))
#
#sources.append(source('gl4', docbook_parser(),
#    regexp=r'^gl[A-Z][a-zA-Z0-9]*\.xml$',
#    xpath='//file/@name',
#    index='https://cvs.khronos.org/svn/repos/ogl/trunk/ecosystem/public/sdk/docs/man4/',
#    base='http://www.opengl.org/sdk/docs/man4/'))
#
#sources.append(source('glu', docbook_parser(),
#    regexp=r'^glu[A-Z][a-zA-Z0-9]*\.xml$',
#    xpath='//file/@name',
#    index='https://cvs.khronos.org/svn/repos/ogl/trunk/ecosystem/public/sdk/docs/man/',
#    base='http://www.opengl.org/sdk/docs/man/'))
#
#sources.append(source('glX', docbook_parser(),
#    regexp=r'^glX[A-Z][a-zA-Z0-9]*\.xml$',
#    xpath='//file/@name',
#    index='https://cvs.khronos.org/svn/repos/ogl/trunk/ecosystem/public/sdk/docs/man/',
#    base='http://www.opengl.org/sdk/docs/man/'))
#
#sources.append(source('glext', extension_parser(),
#    regexp=r'^specs/[A-Z]+/[a-zA-Z0-9_]+\.txt$',
#    xpath='//a/@href',
#    index='http://www.opengl.org/registry/',
#    base='http://www.opengl.org/registry/'))

sources.append(source('gl', dotspec_constant_parser,
    regexp=r'^api/enumext\.spec$',
    xpath='//a/@href',
    index='http://www.opengl.org/registry/',
    base='http://www.opengl.org/registry/'))

sources.append(source('glX', dotspec_constant_parser,
    regexp=r'^api/glxenumext\.spec$',
    xpath='//a/@href',
    index='http://www.opengl.org/registry/',
    base='http://www.opengl.org/registry/'))

sources.append(source('wgl', dotspec_constant_parser,
    regexp=r'^api/wglenumext\.spec$',
    xpath='//a/@href',
    index='http://www.opengl.org/registry/',
    base='http://www.opengl.org/registry/'))

sources.append(source('egl', dotspec_constant_parser,
    regexp=r'^api/eglenum\.spec$',
    xpath='//a/@href',
    index='http://www.khronos.org/registry/egl/',
    base='http://www.khronos.org/registry/egl/'))

sources.append(source('gl', dotspec_function_parser,
    regexp=r'^api/gl(?:ext)?\.spec$',
    xpath='//a/@href',
    index='http://www.opengl.org/registry/',
    base='http://www.opengl.org/registry/'))

sources.append(source('glX', dotspec_function_parser,
    regexp=r'^api/glx(?:ext)?\.spec$',
    xpath='//a/@href',
    index='http://www.opengl.org/registry/',
    base='http://www.opengl.org/registry/'))

sources.append(source('wgl', dotspec_function_parser,
    regexp=r'^api/wgl(?:ext)?\.spec$',
    xpath='//a/@href',
    index='http://www.opengl.org/registry/',
    base='http://www.opengl.org/registry/'))

sources.append(source('gl', dottm_parser,
    regexp=r'^api/[a-z]+\.tm$',
    xpath='//a/@href',
    index='http://www.opengl.org/registry/',
    base='http://www.opengl.org/registry/'))

for s in sources:
  s.parse()

def printall():
  for c in raw_constants:
    li = library.get(c.stack.library_name)
    gr = li.groups[c.stack.extension_name]
    ex = gr.extensions[c.stack.extension_name]
    ca = ex.categories[c.stack.category_name]

    if not c.name in ca.constants:
      ca.constants[c.name] = c
    elif c.value != ca.constants[c.name].value:
      log.warn('C %s (%s, %s) already in %s.%s.%s' % (c.name, c.value, ca.constants[c.name].value, li.name, ex.name, ca.name))

  for f in raw_functions:
    li = library.get(f.stack.library_name)
    gr = li.groups[f.stack.extension_name]
    ex = gr.extensions[f.stack.extension_name]
    ca = ex.categories[f.stack.category_name]

    if not f.name in ca.functions:
      ca.functions[f.name] = f
    else:
      log.warn('F %s already in %s.%s.%s' % (f.name, li.name, ex.name, ca.name))

  for li in libraries.values():
    print 'L:', li.name
    for gr in li.groups.values():
      print ' G:', gr.name
      for ex in gr.extensions.values():
        print '  E:', ex.name
        for ca in ex.categories.values():
          print '   C:', ca.name
          print '    c:'
          for c in ca.constants.values():
            print '     ', c.name, ' = ', c.value
          print '    f:'
          for f in ca.functions.values():
            print '     ', f.name

printall()

#print '#include <cstdint>'
#for n in sorted(set([ e.name for e in enums ])):
#  print 'enum class', n, ': std::uint32_t {'
#  for v, c in sorted(set([ (c.value, c.name) for c in constants if c.enum_name == n])):
#    print '  ', c, '=', v, ','
#  print '};'
