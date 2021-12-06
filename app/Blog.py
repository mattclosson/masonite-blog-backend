"""Blog Model."""

from masoniteorm.models import Model


class Blog(Model):
    __table__="blogs"
    