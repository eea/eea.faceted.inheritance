from zope import interface
from eea.faceted.inheritance.subtypes.interfaces import IFacetedHeritor
from p4a.subtyper.interfaces import IPortalTypedFolderishDescriptor

class FacetedHeritorDescriptor(object):
    """ Abstract report descriptor
    """
    interface.implements(IPortalTypedFolderishDescriptor)
    title = u'Faceted Heritor'
    description = u'Faceted heritor'
    type_interface = IFacetedHeritor

class FolderFacetedHeritorDescriptor(FacetedHeritorDescriptor):
    """ Folder descriptor
    """
    for_portal_type = 'Folder'

class LargeFolderFacetedHeritorDescriptor(FacetedHeritorDescriptor):
    """ Large Folder descriptor
    """
    for_portal_type = 'Large Plone Folder'

class TopicFacetedHeritorDescriptor(FacetedHeritorDescriptor):
    """ Topic descriptor
    """
    for_portal_type = 'Topic'

class RichTopicFacetedHeritorDescriptor(FacetedHeritorDescriptor):
    """ RichTopic descriptor
    """
    for_portal_type = 'RichTopic'
