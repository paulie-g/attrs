from __future__ import absolute_import, division, print_function

from attr import Attribute
from attr._make import NOTHING, make_class


def simple_class(cmp=False, repr=False, hash=False):
    """
    Return a new simple class.
    """
    return make_class(
        "C", ["a", "b"],
        cmp=cmp, repr=repr, hash=hash, init=True,
    )


def simple_attr(name, default=NOTHING, validator=None, repr=True,
                cmp=True, hash=True, init=True):
    """
    Return an attribute with a name and no other bells and whistles.
    """
    return Attribute(
        name=name, default=default, validator=validator, repr=repr,
        cmp=cmp, hash=hash, init=init
    )


class TestSimpleClass(object):
    """
    Tests for the testing helper function `make_class`.
    """
    def test_returns_class(self):
        """
        Returns a class object.
        """
        assert type is simple_class().__class__

    def returns_distinct_classes(self):
        """
        Each call returns a completely new class.
        """
        assert simple_class() is not simple_class()
