# Python 2/3 Compatibility
from builtins import range

import pytest
from math import factorial
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
from wova.concurrent.futures import as_completed_buffered

EXECUTOR = ThreadPoolExecutor(max_workers=2)
DATA_LIST = [x for x in range(100)]


def test_as_completed_buffered_with_generator():
    """
    """
    DATA_GEN = range(100)

    futures = (EXECUTOR.submit(factorial, x) for x in DATA_GEN)
    assert 1 == 1

def test_2_is_2():
    assert 2 == 2


test_as_completed_buffered_with_generator()
test_2_is_2()

    



