import math

import scipy


def f(x):
    return math.sin(x) - math.cos(x)


def single_integral(a, b):
    return scipy.quad(f, a, b)


def add(a, b):
    return a + b


def record(value, history=None):
    if history is None:
        history = []
    history.append(value)
    return history


def broken_total():
    return missing_totals
