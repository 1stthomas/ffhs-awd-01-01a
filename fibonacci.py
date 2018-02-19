# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 17:53:56 2018

@author: ctsoft
"""
import time
import ctsoft.awd.sequences.fibonacci as fibonacci


"""
@var step : the step of the fibunacci sequence to be calculated.
"""
step = 30

print("---------------------------")
print("step: " + str(step))
t_start = time.process_time()
fibonacci.printOutput("fib(" + str(step) + ")", "value", fibonacci.fib(step))
t_end = time.process_time()
print("Zeitdifferenz: " + str(t_end - t_start))
print("---------------------------")
print("step: " + str(step))
t_start = time.process_time()
fibonacci.printOutput("fib1(" + str(step) + ")", "value", fibonacci.fib1(step))
t_end = time.process_time()
print("Zeitdifferenz: " + str(t_end - t_start))
print("---------------------------")
fibonacci.fib2.count = 0
fibonacci.printOutput("fib2(" + str(step) + ")", "value", fibonacci.fib2(step))
fibonacci.printOutput("fib2(" + str(step) + ")", "count", fibonacci.fib2.count)
print("---------------------------")
count = fibonacci.fibCallsCount(step)
fibonacci.printOutput("fibCallsCount(" + str(step) + ", 0)", "count", count)
