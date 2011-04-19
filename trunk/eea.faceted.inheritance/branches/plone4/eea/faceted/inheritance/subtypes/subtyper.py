""" Subtyping support
"""
from zope.interface import implements
from zope.interface import alsoProvides, noLongerProvides
from zope.event import notify
from zope.publisher.interfaces import NotFound

from p4a.subtyper.engine import SubtypeAddedEvent, SubtypeRemovedEvent
from Products.statusmessages.interfaces import IStatusMessage
from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName

from eea.faceted.inheritance.subtypes.interfaces import IFacetedHeritorSubtyper
from eea.facetednavigation.subtypes.subtyper import FacetedPublicSubtyper

from eea.faceted.inheritance.interfaces import IPossibleFacetedHeritor
from eea.faceted.inheritance.interfaces import IFacetedHeritor

class FacetedHeritorPublicSubtyper(FacetedPublicSubtyper):
    """ Public support for subtyping objects
    """
    implements(IFacetedHeritorSubtyper)

    @property
    def can_enable_heritor(self):
        """ See IFacetedHeritorSubtyper
        """
        if not IPossibleFacetedHeritor.providedBy(self.context):
            return False

        if IFacetedHeritor.providedBy(self.context):
            return False
        return True

class FacetedHeritorSubtyper(FacetedHeritorPublicSubtyper):
    """ Support for subtyping objects
    """
    def enable(self):
        """ See IFacetedSubtyper
        """
        if not self.can_enable_heritor:
            return self._redirect('Faceted inheritance not supported')

        if not IFacetedHeritor.providedBy(self.context):
            alsoProvides(self.context, IFacetedHeritor)

        notify(SubtypeAddedEvent(self.context, None))
        self._redirect('Faceted inheritance enabled')
