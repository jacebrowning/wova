# Python 2/3 Compatibility
from builtins import range

import pytest   # NOQA # Flake8 ignore 
from wova import enumerators as em
from wova.enumerators._base import seconds_to_human_string


def test_monitor_generator():
    """
    Test monitor with a generator
    """
    DATA_GEN = range(100)

    # Standard Library
    sl = [(ix, v) for ix, v in enumerate(DATA_GEN)]

    # Non-Standard Library
    nsl = [(ix, v) for ix, v in em.monitor(enumerate(DATA_GEN))]

    assert sl == nsl


def test_monitor_list():
    """
    Test monitor with a generator
    """
    DATA_LIST = [(ix, v) for ix, v in enumerate(range(100))]

    # Standard Library
    sl = [(ix, v) for ix, v in em.monitor(DATA_LIST)]

    # Non-Standard Library
    nsl = [(ix, v) for ix, v in em.monitor(DATA_LIST)]

    assert sl == nsl


def test_seconds_to_human_string():
    """
    Test seconds to human readable string function
    """

    assert seconds_to_human_string(8) == '08s'
    assert seconds_to_human_string(103) == '01m 43s'
    assert seconds_to_human_string(1088) == '18m 08s'
    assert seconds_to_human_string(10000) == '2h 46m 40s'
    assert seconds_to_human_string(100000) == '1d 3h 46m 40s'
