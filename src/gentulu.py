#!/usr/bin/python
# -*- coding: utf-8 -*-

# Distributed under the Boost Software License, Version 1.0.
# See accompanying file LICENSE or copy at http://www.boost.org/LICENSE

from lxml import etree, html
from resolver import resolver
import re
from parser.docbook import docbook_parser
from parser.extension import extension_parser
from parser.dotspec import dotspec_parser
from parser.dottm import dottm_parser
from utils import log, option_parser, print_help
from object.enum import enums
from object.constant import constants

parser = option_parser()
(o, a) = parser.parse_args()

# Registering the Resolver as the default DTD Resolver
xml_parser = etree.XMLParser(load_dtd=True)
xml_parser.resolvers.add(resolver())
etree.set_default_parser(xml_parser)

class source(object):
  def __init__(self, name, parser, **kwargs):
    self.name = name
    self.parser = parser
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
      log.debug(self.name + ': ' + f)

  def parse(self):
    for url in self.files:
      local_file = resolver.cache(url)
      self.parser.parse(local_file)

sources = []

# 'base' and 'index' shoud be the same in 99% of cases,
# but it's faster to download .xml on http rather than webdav over https
sources.append(source('gl2', docbook_parser(),
    regexp=r'^gl[A-Z][a-zA-Z0-9]*\.xml$',
    xpath='//file/@name',
    index='https://cvs.khronos.org/svn/repos/ogl/trunk/ecosystem/public/sdk/docs/man/',
    base='http://www.opengl.org/sdk/docs/man/'))

sources.append(source('gl3', docbook_parser(),
    regexp=r'^gl[A-Z][a-zA-Z0-9]*\.xml$',
    xpath='//file/@name',
    index='https://cvs.khronos.org/svn/repos/ogl/trunk/ecosystem/public/sdk/docs/man3/',
    base='http://www.opengl.org/sdk/docs/man3/'))

sources.append(source('gl4', docbook_parser(),
    regexp=r'^gl[A-Z][a-zA-Z0-9]*\.xml$',
    xpath='//file/@name',
    index='https://cvs.khronos.org/svn/repos/ogl/trunk/ecosystem/public/sdk/docs/man4/',
    base='http://www.opengl.org/sdk/docs/man4/'))

sources.append(source('glu', docbook_parser(),
    regexp=r'^glu[A-Z][a-zA-Z0-9]*\.xml$',
    xpath='//file/@name',
    index='https://cvs.khronos.org/svn/repos/ogl/trunk/ecosystem/public/sdk/docs/man/',
    base='http://www.opengl.org/sdk/docs/man/'))

sources.append(source('glX', docbook_parser(),
    regexp=r'^glX[A-Z][a-zA-Z0-9]*\.xml$',
    xpath='//file/@name',
    index='https://cvs.khronos.org/svn/repos/ogl/trunk/ecosystem/public/sdk/docs/man/',
    base='http://www.opengl.org/sdk/docs/man/'))

sources.append(source('glext', extension_parser(),
    regexp=r'^specs/[A-Z]+/[a-zA-Z0-9_]+\.txt$',
    xpath='//a/@href',
    index='http://www.opengl.org/registry/',
    base='http://www.opengl.org/registry/'))

sources.append(source('glenums', dotspec_parser('gl'),
    regexp=r'^api/enumext\.spec$',
    xpath='//a/@href',
    index='http://www.opengl.org/registry/',
    base='http://www.opengl.org/registry/'))

sources.append(source('glenums', dotspec_parser('glX'),
    regexp=r'^api/glxenumext\.spec$',
    xpath='//a/@href',
    index='http://www.opengl.org/registry/',
    base='http://www.opengl.org/registry/'))

sources.append(source('glenums', dotspec_parser('wgl'),
    regexp=r'^api/wglenumext\.spec$',
    xpath='//a/@href',
    index='http://www.opengl.org/registry/',
    base='http://www.opengl.org/registry/'))

#sources.append(source('glfuncs', dotspec_parser(),
#    regexp=r'^api/w?glx?(?:ext)?\.spec$',
#    xpath='//a/@href',
#    index='http://www.opengl.org/registry/',
#    base='http://www.opengl.org/registry/'))
#
#sources.append(source('gltypes', dottm_parser(),
#    regexp=r'^api/[a-z]+\.tm$',
#    xpath='//a/@href',
#    index='http://www.opengl.org/registry/',
#    base='http://www.opengl.org/registry/'))

for s in sources:
  s.parse()

for n in sorted(set([ e.name for e in enums ])):
  print 'enum class', n, '{'
  for v, c in sorted(set([ (c.value, c.name) for c in constants if c.enum_name == n])):
    print '  ', c, '=', v, ','
  print '};'
