from zope.interface import Interface
from zope.interface import Interface, alsoProvides
from zope.app.content.interfaces import IContentType
from eea.facetednavigation.interfaces import IFacetedNavigable

class IPossibleFacetedHeritor(Interface):
    """
    A possible heritor that can inherit faceted configuration from a
    faceted navigable object.
    """

class IFacetedHeritor(IFacetedNavigable):
    """
    A heritor that inherit faceted configuration from a
    faceted navigable object.
    """

alsoProvides(IFacetedHeritor, IContentType)
