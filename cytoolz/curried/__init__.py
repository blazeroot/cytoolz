###############################################################################
# THIS FILE IS AUTOMATICALLY GENERATED                                        #
#                                                                             #
# Please make all edits in etc/generate_curried.py and re-run                 #
# cytoolz/tests/test_curried_toolzlike.py                                     #
###############################################################################
"""
Alternate namespece for cytoolz such that all functions are curried

Currying provides implicit partial evaluation of all functions

Example:

    Get usually requires two arguments, an index and a collection
    >>> from cytoolz.curried import get
    >>> get(0, ('a', 'b'))
    'a'

    When we use it in higher order functions we often want to pass a partially
    evaluated form
    >>> data = [(1, 2), (11, 22), (111, 222)]
    >>> list(map(lambda seq: get(0, seq), data))
    [1, 11, 111]

    The curried version allows simple expression of partial evaluation
    >>> list(map(get(0), data))
    [1, 11, 111]

See Also:
    cytoolz.functoolz.curry
"""
from . import exceptions
from . import operator
import cytoolz


_curry_set = frozenset([
    cytoolz.accumulate,
    cytoolz.assoc,
    cytoolz.assoc_in,
    cytoolz.cons,
    cytoolz.countby,
    cytoolz.do,
    cytoolz.drop,
    cytoolz.excepts,
    cytoolz.filter,
    cytoolz.flip,
    cytoolz.get,
    cytoolz.get_in,
    cytoolz.groupby,
    cytoolz.interleave,
    cytoolz.interpose,
    cytoolz.itemfilter,
    cytoolz.itemmap,
    cytoolz.iterate,
    cytoolz.join,
    cytoolz.keyfilter,
    cytoolz.keymap,
    cytoolz.map,
    cytoolz.mapcat,
    cytoolz.memoize,
    cytoolz.merge,
    cytoolz.merge_with,
    cytoolz.nth,
    cytoolz.partial,
    cytoolz.partition,
    cytoolz.partition_all,
    cytoolz.partitionby,
    cytoolz.pluck,
    cytoolz.random_sample,
    cytoolz.reduce,
    cytoolz.reduceby,
    cytoolz.remove,
    cytoolz.sliding_window,
    cytoolz.sorted,
    cytoolz.tail,
    cytoolz.take,
    cytoolz.take_nth,
    cytoolz.topk,
    cytoolz.unique,
    cytoolz.update_in,
    cytoolz.valfilter,
    cytoolz.valmap,
])


def _curry_namespace(ns):
    return dict(
        (name, cytoolz.curry(f) if f in _curry_set else f)
        for name, f in ns.items() if '__' not in name
    )


locals().update(cytoolz.merge(
    _curry_namespace(vars(cytoolz)),
    _curry_namespace(vars(exceptions)),
))

# Clean up the namespace.
del _curry_set
del _curry_namespace
del exceptions
del cytoolz

