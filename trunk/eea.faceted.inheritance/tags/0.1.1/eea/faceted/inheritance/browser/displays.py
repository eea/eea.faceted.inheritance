""" Faceted views
"""
from zope.interface import implements
from zope.component import queryAdapter
from Products.CMFDynamicViewFTI.interfaces import IDynamicallyViewable
from eea.faceted.inheritance.interfaces import ICriteria
class HeritorViews(object):
    """ Display
    """
    implements(IDynamicallyViewable)

    def __init__(self, context):
        self.context = context

    def getAvailableViewMethods(self):
        """Get a list of registered view method names
        """
        return [view for view, name in self.getAvailableLayouts()]

    def getDefaultViewMethod(self):
        """Get the default view method name
        """
        accessor = queryAdapter(self.context, ICriteria)
        if not accessor:
            return 'facetedheritor_view'
        if not accessor.ancestor:
            return 'facetedheritor_view'
        return 'facetednavigation_view'

    def getAvailableLayouts(self):
        """Get the layouts registered for this object.
        """
        return (("facetednavigation_view", "Faceted View"),)
