"""
interfaces.py

Interfaces to commonly used plt methods, bypassing object oriented approach

    - Author: Henry Pickersgill (2026)
"""
from easy_plot import Figure, plt

__all__ = ["plot", "show"]

def plot(*args, **kwargs):
    fig = Figure()
    fig.plot(*args, *kwargs)


def scatter(*args, **kwargs):
    fig = Figure()
    fig.plot(*args, **kwargs)


def display():
    """
    Interface to Figure.display()
    Shows all Figure objects marked as visible with fig.show().
    If no Figures are marked as visible, calling this function
    will show all created Figures
    """
    Figure.display()
