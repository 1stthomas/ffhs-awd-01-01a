# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 19:03:59 2018

@author: zoom4u
"""

index = 0


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
    global index
    index = index + 1
    
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def fibCallsCount(n):
    print(fibCallsCount.count)
    fibCallsCount.count = fibCallsCount.count + 1
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(10))
print("---------------------------")
print("index: " + str(index))
print("---------------------------")

fibCallsCount.count = 0

print(fibCallsCount(10))
print("---------------------------")
print("count: " + str(fibCallsCount.count))
