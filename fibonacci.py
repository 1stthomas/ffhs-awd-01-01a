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
value1 = fibonacci.fib(step)
t_end = time.process_time()
fibonacci.printOutput("fib(" + str(step) + ")", "value", value1)
print("Zeitdifferenz: " + str(t_end - t_start))
print("---------------------------")
print("step: " + str(step))
t_start = time.process_time()
value2 = fibonacci.fib1(step)
t_end = time.process_time()
fibonacci.printOutput("fib1(" + str(step) + ")", "value", value2)
print("Zeitdifferenz: " + str(t_end - t_start))
t_start = time.process_time()
value3 = fibonacci.fib1(step)
count1 = fibonacci.fibCallsCount(step)
t_end = time.process_time()
fibonacci.printOutput("fib1(" + str(step) + ")", "value", value3)
fibonacci.printOutput("fibCallsCount(" + str(step) + ", 0)", "count", count1)
print("Zeitdifferenz mit zusätzlicher Zählung: " + str(t_end - t_start))
print("---------------------------")
t_start = time.process_time()
fibonacci.fib2.count = 0
value4 = fibonacci.fib2(step)
t_end = time.process_time()
fibonacci.printOutput("fib2(" + str(step) + ")", "value", value4)
fibonacci.printOutput("fib2(" + str(step) + ")", "count", fibonacci.fib2.count)
msg = "Zeitdifferenz mit zusätzlicher Zählung der Funktionsaufrufen: "
print(msg + str(t_end - t_start))
print("---------------------------")
