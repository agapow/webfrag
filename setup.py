from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='webfrag',
      version=version,
      description="Tools for generating and merging 'fragments' of HTML and embedded media for webservices",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='web media resource',
      author='Paul-Michael Agapow',
      author_email='agapow@bbsrc.ac.uk',
      url='http://www.agapow.net/software/webfrag',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
