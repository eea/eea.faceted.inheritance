""" EEA Faceted Inheritance
"""
# Plone 2.5 Backward compatible
try:
    from Products.CMFPlone.CatalogTool import _eioRegistry
    def object_provides(object, portal, **kw):
        return [i.__identifier__ for i in providedBy(object).flattened()]

    if not _eioRegistry.has_key('object_provides'):
        _eioRegistry.register('object_provides', object_provides)
except ImportError, err:
    pass
