#!/usr/bin/python
# -*- coding: utf-8 -*-

# Distributed under the Boost Software License, Version 1.0.
# See accompanying file LICENSE or copy at http://www.boost.org/LICENSE

# Contains code from Alexandre Fournier's gl-spec-parser
# https://github.com/AlexandreFournier/gl-spec-parser

import os
from lxml import etree
from urlparse import urlparse
from urllib import urlretrieve
from utils import log

class resolver(etree.Resolver):
  # Caching should be done in urllib
  CACHE_PATH = '../data'

  @staticmethod
  def cache(system_url):
    url = urlparse(system_url)
    if url.scheme == '':
      if url.path.startswith(resolver.CACHE_PATH):
        system_url = system_url.replace(resolver.CACHE_PATH, 'file://')
        url = urlparse(system_url)

    if url.scheme in [ 'http', 'https', 'file' ]:
      url_path, url_file = os.path.split(url.path)
      url_path = url_path.replace('/', os.sep)
      url_path = url.hostname + url_path

      local_path = os.path.join(resolver.CACHE_PATH, url_path)
      local_file = os.path.join(local_path, url_file)

      if not os.path.exists(local_path):
        os.makedirs(local_path)

      if local_file.endswith(os.sep):
        local_file += 'INDEX'

      if not os.path.exists(local_file):
        log.info('retrieving %s...' % system_url)

        urlretrieve(system_url, local_file)

      return local_file

    return None

  def resolve(self, system_url, system_id, context):
    local_file = resolver.cache(system_url)
    if not local_file == None:
      return self.resolve_filename(local_file, context)

