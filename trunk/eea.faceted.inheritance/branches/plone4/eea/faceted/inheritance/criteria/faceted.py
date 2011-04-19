""" Faceted criteria
"""
from zope.interface import implements
from zope.component import queryAdapter

from eea.faceted.inheritance.criteria.interfaces import ICriteria
from eea.faceted.inheritance.criteria.interfaces import IHeritorAccessor

from Products.CMFCore.utils import getToolByName

class Criteria(object):
    """ Overrides default facetednavigation functionality
    """
    implements(ICriteria)

    def _ancestor(self, context):
        """ Get ancestor
        """
        handler = queryAdapter(context, IHeritorAccessor)
        path = handler.ancestor
        ctool = getToolByName(context, 'portal_catalog')
        brains = ctool(path={'query': path, 'depth': 0})
        for brain in brains:
            return brain.getObject()
        return None

    def __init__(self, context):
        self.ancestor = self._ancestor(context)
        self.context = self.ancestor or context
        self.adapter = queryAdapter(self.ancestor, ICriteria)
    #
    # Getters
    #
    @property
    def criteria(self):
        """ Get faceted criteria from ancestor
        """
        if not self.ancestor:
            return []
        return self.ancestor.criteria

    def newid(self):
        """ Faceted criterion new id
        """
        if not self.adapter:
            return ''
        return self.adapter.newid()

    def get(self, key, default=None):
        """ Get faceted criterion by id from ancestor
        """
        if not self.adapter:
            return default
        return self.adapter.get(key, default)

    def keys(self):
        """ Faceted criteria keys from ancestor
        """
        if not self.adapter:
            return []
        return self.adapter.keys()

    def values(self):
        """ Faceted criteria values from ancestor
        """
        if not self.adapter:
            return []
        return self.adapter.values()

    def items(self):
        """ Faceted criteria items from ancestor
        """
        if not self.adapter:
            return []
        return self.adapter.items()
    #
    # Setters
    #
    def add(self, *args, **kwargs):
        """
        As this is a read-only proxy to a faceted navigable object
        adding widgets is forbidden
        """
        return

    def delete(self, cid):
        """
        As this is a read-only proxy to a faceted navigable object
        deleting widgets is forbidden
        """
        return

    def edit(self, *args, **kwargs):
        """
        As this is a read-only proxy to a faceted navigable object
        editing widgets is forbidden
        """
        return
    #
    # Position
    #
    def up(self, cid):
        """
        As this is a read-only proxy to a faceted navigable object
        moving widgets is forbidden
        """
        return

    def down(self, cid):
        """
        As this is a read-only proxy to a faceted navigable object
        moving widgets is forbidden
        """
        return

    def position(self, **kwargs):
        """
        As this is a read-only proxy to a faceted navigable object
        moving widgets is forbidden
        """
        return
    #
    # Utils
    #
    def widget(self, wid=None, cid=None):
        """ Faceted widget from ancestor
        """
        if not self.adapter:
            raise KeyError(cid)
        return self.adapter.widget(wid, cid)
