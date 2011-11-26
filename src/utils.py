#!/usr/bin/python
# -*- coding: utf-8 -*-

# Distributed under the Boost Software License, Version 1.0.
# See accompanying file LICENSE or copy at http://www.boost.org/LICENSE

import sys
import os
import logging
import logutils.colorize
from optparse import OptionParser

def init_logging(script_name):
  # define a Handler which writes INFO messages or higher to the sys.stderr
  console = logutils.colorize.ColorizingStreamHandler()
  console.setLevel(logging.DEBUG)

  if '--info' in sys.argv:
    console.setLevel(logging.INFO)
  if '--warning' in sys.argv:
    console.setLevel(logging.WARNING)
  if '--error' in sys.argv:
    console.setLevel(logging.ERROR)

  # set a format which is simpler for console use
  formatter = logging.Formatter('%s: %s' % (script_name, '%(message)s'))

  # tell the handler to use this format
  console.setFormatter(formatter)

  # add the handler to the root logger
  root = logging.getLogger('')
  root.addHandler(console)
  root.setLevel(logging.DEBUG)

script_name = os.path.basename(sys.argv[0]).replace('.py', '')
init_logging(script_name)

log = logging.getLogger('')

def print_help(option, opt, value, parser):
  parser.print_help(sys.stderr)
  sys.exit(1)

def option_parser(positionals=""):
  parser = OptionParser(usage="usage: %prog [options] " + positionals, prog=script_name, add_help_option=False)
  parser.add_option("-h", "--help", help="show this help message and exit", action="callback", callback=print_help)
  parser.add_option("-f", "--force", default=False, dest="force", help="apply operations (default: dry run)", action="store_true")
  parser.add_option("--info", action="store_true")
  parser.add_option("--warning", action="store_true")
  parser.add_option("--error", action="store_true")

  return parser

