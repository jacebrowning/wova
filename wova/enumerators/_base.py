from __future__ import print_function, division
import sys
import time


def seconds_to_human_string(seconds):
    """
    Purpose:
        Convert a number of seconds into a human friendly string in days,
        hours, minutes, and seconds.

    Args:
        seconds = number of seconds (int or float)

    Output:
        a human friendly string
    """

    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    if sum([d, h, m]) == 0:
        return "%02ds" % s
    elif sum([d, h]) == 0:
        return "%02dm %02ds" % (m, s)
    elif d == 0:
        return "%dh %02dm %02ds" % (h, m, s)
    else:
        return "%dd %dh %02dm %02ds" % (d, h, m, s)


def monitor(iterable, length=None):
    """
    Purpose:
        Wraps an iterable and prints progress stats as it is consumed

    Args:
        iterable = an iterable object
        length = Optional
                 If iterable is a generator, passing length adds a completion
                    time to the output
                 If omitted, time to completion is not computed.

    Output:
        A generator that yields values from iterable and prints output
        statistics as consumed
    """

    def print_status(idx, elapsed_time, known_length, end='\r'):
        # if length is unknown
        if not known_length:
            print('Row: %8d\t\tElapsed Time: %8s' %
                  (idx, seconds_to_human_string(elapsed_time)), end=end)

        # Print all results if iterable has a len()
        else:
            remaining_time = ((elapsed_time/ix)*known_length)-elapsed_time
            print('Row: %8d\t\tElapsed Time: %8s\t\t Time Remaining: %8s' %
                  (idx,
                   seconds_to_human_string(elapsed_time),
                   seconds_to_human_string(remaining_time)
                   ), end=end)
        sys.stdout.flush()

    # Get length of iterable is available
    length = len(iterable) if hasattr(iterable, '__len__') else length

    # Start timers
    timer = time.time()
    t_total = 0

    # Most recent timer check
    last_time = timer

    for ix, value in enumerate(iterable):

        # If no update in the last 1 second
        current_time = time.time()

        if current_time - last_time > 0.5:

            # Reset Last Time
            last_time = current_time

            # Total Elapsed Time
            t_total = current_time - timer

            # Print status
            print_status(ix, t_total, length)

        yield value

    # Print status on final value
    print_status(ix, t_total, length, end='\n')
    print('Done')
    return


def rate_limit(iterable, per_second=None, per_minute=None, per_hour=None):
    """
    Purpose:
        Wraps an iterable with a rate limiter

    Args:
        iterable = an iterable object
        per_second = Limit iterations per second
        per_minute = Limit iterations per minute
        per_hour   = Limit iterations per hour

    Note:
        If no rate is passed to per_second, per_minute, or per_hour then
        the iterator will not be rate limited

        Only 1 of per_second, per_minute, per_hour, should be passed

    Output:
        A generator that yields values from iterable subject to a rate limit
    """

    # TODO: Update so the first n values yield immediately and then sleep

    # Compute wait time
    if per_second:
        wait_seconds = 1/per_second
    elif per_minute:
        wait_seconds = 60/per_minute
    elif per_hour:
        wait_seconds = 3600/per_hour

    for v in iterable:
        yield v
        time.sleep(wait_seconds)

    return
















