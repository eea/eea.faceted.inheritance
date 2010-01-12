""" Doc tests
"""
import unittest
from zope.testing import doctest
from Testing.ZopeTestCase import FunctionalDocFileSuite as Suite
from base import FacetedInheritanceFunctionalTestCase

OPTIONFLAGS = (doctest.REPORT_ONLY_FIRST_FAILURE |
               doctest.ELLIPSIS |
               doctest.NORMALIZE_WHITESPACE)

def test_suite():
    """ Suite
    """
    return unittest.TestSuite((
            Suite('README.txt',
                  optionflags=OPTIONFLAGS,
                  package='eea.faceted.inheritance',
                  test_class=FacetedInheritanceFunctionalTestCase) ,
            Suite('docs/browser.txt',
                  optionflags=OPTIONFLAGS,
                  package='eea.faceted.inheritance',
                  test_class=FacetedInheritanceFunctionalTestCase),
            Suite('docs/inheritance.txt',
                  optionflags=OPTIONFLAGS,
                  package='eea.faceted.inheritance',
                  test_class=FacetedInheritanceFunctionalTestCase),
    ))
