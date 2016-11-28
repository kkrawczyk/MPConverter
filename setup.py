#!/usr/bin/env python

from distutils.core import setup

setup(name='MPParser',
      version='1.0.0',
      description='MP parser',
      author='Krzysztof Krawczyk',
      author_email='krzysztof@krawczyk.czest.pl',
      url='https://www.nova-it.eu/',
      packages=['MPParser', 'MPParser.Sections', 'MPParser.Utils'],
     )