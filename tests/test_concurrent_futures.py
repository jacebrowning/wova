# Python 2/3 Compatibility
from builtins import range

import pytest   # NOQA # Flake8 ignore 
from math import factorial
from concurrent.futures import ThreadPoolExecutor, as_completed
from wova.concurrent.futures._base import as_completed_buffered

EXECUTOR = ThreadPoolExecutor(max_workers=2)


def test_as_completed_buffered_with_list():
    """
    Test as_completed_buffered with a list of futures input
    """
    DATA_GEN = range(100)

    futures = [EXECUTOR.submit(factorial, x) for x in DATA_GEN]
    sl = sorted([x.result() for x in as_completed(futures)])
    nsl = sorted([x.result() for x in as_completed_buffered(futures, 4)])

    assert sl == nsl


def test_as_completed_buffered_with_generator():
    """
    Test as_completed_buffered with a generator of futures input
    """
    DATA_GEN = range(100)

    def data_to_future_gen(dat):
        return (EXECUTOR.submit(factorial, x) for x in dat)

    # Standard Library
    futures_sl = data_to_future_gen(DATA_GEN)
    sl = sorted([x.result() for x in as_completed(futures_sl)])

    # Non-standard Library
    futures_nsl = data_to_future_gen(DATA_GEN)
    nsl = sorted([x.result() for x in as_completed_buffered(futures_nsl, 4)])

    assert sl == nsl
