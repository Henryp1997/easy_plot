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


def show():
    plt.show()
