from __future__ import unicode_literals, print_function, division
from builtins import zip
from collections import deque
from concurrent.futures import as_completed
from itertools import count as icount


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
    # Convert any input sequence into a consumable generator
    future_gen = (x for x in future_iterable)

    # Use buffer if provided, else use inf
    b_rng = range(buffer_size) if buffer_size else icount()

    # Currently Submitted Futures
    buf = deque(x for _, x in zip(b_rng, future_gen))

    for future in future_gen:

        # Return the first available future
        v_ready = next(as_completed(buf))
        yield v_ready

        # Remove completed future from the buffer
        # Slow. This could use work
        # Used a list comprehension to avoid filter function call overhead
        buf = [x for x in buf if x != v_ready]

        # Replace the completed work on the buffer
        buf.append(future)

    # Once the iterable of futures is exhausted
    # Yield remaining work from the buffer as it completes
    for x in as_completed(buf):
        yield x

    return
