from __future__ import print_function
import sys
import time
from inspect import isgenerator


def seconds_to_human_string(seconds):
    """
    Purpose:
        Convert a number of seconds into a human friendly string in days, hours, minutes, and seconds.

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
        Wraps an iterable and prints progress statistics as that iterable is consumed
    
    Args:
        iterable = an iterable object
        length = Optional. If iterable is a generator a value is needed for length to
                 estimate time until completion. If omitted, time to completion is not computed.
    
    Output:
        A generator that yields values from iterable and prints output statistics as consumed
    """
    
    def print_status(idx, elapsed_time, generator_fl, known_length, end='\r'):
        # Print partial results if iterable has no len() and argument 'length' not passed e.g. a generator
        if generator_fl and not known_length:
            print('Row: %8d\t\tElapsed Time: %8s' % 
                  (idx, 
                   seconds_to_human_string(elapsed_time)
                  ), end=end)
        # Print all results if iterable has a len()
        else:
            print('Row: %8d\t\tElapsed Time: %8s\t\t Time Remaining: %8s' % 
                  (idx, 
                   seconds_to_human_string(elapsed_time),
                   seconds_to_human_string(((elapsed_time/ix)*known_length)-elapsed_time)
                  ), end=end)
        sys.stdout.flush()
    
    
    # Is the iterable a generator?
    is_gen = True if isgenerator(iterable) else False
    
    # Get length of iterable is available
    length = len(iterable) if not is_gen else length
    
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
            print_status(ix, t_total, is_gen, length)
            
        yield value
        
    # Print status on final value
    print_status(ix, t_total, is_gen, length, end='\n')
    print('Done')
    return

