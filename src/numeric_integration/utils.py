from math import sin, cos

from matplotlib.axes import Axes
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.text import Annotation


def format(fig: Figure, ax: Axes, box_size: int = 0) -> None:

    ax.tick_params(axis='x', colors='#ffffff') #type: ignore
    ax.tick_params(axis='y', colors='#ffffff') #type: ignore

    for spine in ax.spines.values():
        spine.set_color('#ffffff')

    if box_size:
        ax.set_aspect('equal', 'box')
        ax.set_xlim(0, box_size)
        ax.set_ylim(0, box_size)

    ax.set_facecolor('#111117')
    fig.set_facecolor('#111117')
