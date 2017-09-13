from __future__ import unicode_literals, print_function, division
from builtins import zip
from collections import deque
from concurrent.futures import as_completed
from itertools import count


def as_completed_buffered(future_iterable, buffer_size=None):
    """
    Purpose:
        Stream an iterable of futures over an executor with a buffer size.

        Creating futures consumes all of an input iterator before work starts.
        That is a problem when the data set being processed is large because
        it pulls the entire set into memory

    Args:
        future_iterable
            Type: iterable[futures]
            Desc: Iterable of futures to be processed

        buffer_size
            Type: int
            Desc: size for processing buffer

    Yields:
        completed work from the buffer
    """
    
    # Add an index & convert to tuple
    # future_gen = iter(((ix, fut) for ix, fut in enumerate(future_iterable)))
    future_gen = iter(future_iterable)

    # Build the work queue
    if buffer_size:
        buf = [fut for ix, fut in enumerate(future_gen) if ix < buffer_size]
    else:
        buf = [fut for fut in future_gen]

    # Iterate remaining futures from iterable
    for future in future_gen:

        # Return the next available future
        v_ready = next(as_completed(buf))
        yield v_ready

        # Remove completed future from the buffer
        buf = [fut for fut in buf if fut != v_ready]

        # Replace the completed work on the buffer
        buf.append(future)

    # Once the iterable of futures is exhausted
    # Yield remaining work from the buffer as it completes
    for x in as_completed(buf):
        yield x
