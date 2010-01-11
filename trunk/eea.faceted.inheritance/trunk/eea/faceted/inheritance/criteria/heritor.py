try:
    from zope.annotation.interfaces import IAnnotations
except ImportError:
    #BBB Plone 2.5
    from zope.app.annotation.interfaces import IAnnotations

from zope.interface import implements
from eea.faceted.inheritance.config import ANNO_ANCESTOR
from interfaces import IHeritorAccessor

class HeritorAccessor(object):
    """ Criteria handler
    """
    implements(IHeritorAccessor)

    def __init__(self, context):
        self.context = context

    def fget(self, default=None):
        anno = IAnnotations(self.context)
        return anno.get(ANNO_ANCESTOR, '')

    def fset(self, value):
        anno = IAnnotations(self.context)
        anno[ANNO_ANCESTOR] = value

    ancestor = property(fget, fset)
