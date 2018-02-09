# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 19:03:59 2018

@author: zoom4u
"""


def fib(n):
    """
    Calculates the Fibonacci number of the specified step

    Parameters
    ----------
    n : number
      The step to be calculated

    Returns
    -------
    res : number
      The value of the n th step of the Fibonacci

    Example
    -------
    >>> fib(10)
    55
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(10))
