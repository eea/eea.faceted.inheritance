""" Base test cases
"""
import os
from StringIO import StringIO
from Globals import package_home
from cgi import FieldStorage
from ZPublisher.HTTPRequest import FileUpload
from Products.Five import zcml
from Products.Five import fiveconfigure

product_globals = globals()

# Import PloneTestCase - this registers more products with Zope as a side effect
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup

@onsetup
def setup_eea_faceted_inheritance():
    """Set up the additional products.

    The @onsetup decorator causes the execution of this body to be deferred
    until the setup of the Plone site testing layer.
    """
    fiveconfigure.debug_mode = True
    import Products.Five
    zcml.load_config('meta.zcml', Products.Five)

    import eea.faceted.inheritance
    zcml.load_config('configure.zcml', eea.faceted.inheritance)
    fiveconfigure.debug_mode = False

    ptc.installProduct('Five')

    # XXX Plone 2.x compatible
    try: import Products.FiveSite
    except ImportError: pass
    else: ptc.installProduct('FiveSite')

setup_eea_faceted_inheritance()
ptc.setupPloneSite(extension_profiles=('eea.faceted.inheritance:default',))

class FacetedInheritanceTestCase(ptc.PloneTestCase):
    """Base class for integration tests for the 'Faceted Inheritance' product.
    """

class FacetedInheritanceFunctionalTestCase(ptc.FunctionalTestCase, FacetedInheritanceTestCase):
    """Base class for functional integration tests for the 'Faceted Inheritance' product.
    """
