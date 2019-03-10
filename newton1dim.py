#!usr/bin/env python3
# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt

def newton1dim(f, df, x0, eps=1e-10, max_iter=1000):
    x = x0
    iter = 0
    while iter < max_iter:
        x_new = x - f(x)/df(x)
        
        if abs(x_new - x) < eps:
            break;
        x = x_new
        iter += 1
        
    return x_new
    
def f(x):
    return x**3 - 5*x + 1
    
def df(x):
    return 3*x**2 - 5
    
print(newton1dim(f, df, 3))
print(newton1dim(f, df, 0))
print(newton1dim(f, df, -2))
