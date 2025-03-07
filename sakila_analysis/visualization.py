import random
import warnings

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

warnings.filterwarnings('ignore')

DEFAULT_COLOR_MAP = 'viridis'
DEFAULT_COLOR_MAP_GENERATIVE = 'turbo'


def plot_pie_chart(
        data: list, labels: list, title: str,
        percents: bool = False,
        color_map: str | None = None
) -> None:
    """Plots a pie chart."""
    data = data[::-1]
    labels = labels[::-1]

    colors = generate_colors(len(labels), color_map)

    if percents:
        plt.pie(data, labels=labels, colors=colors,
                startangle=180, autopct='%1.2f%%',
                pctdistance=0.75)
    else:
        plt.pie(data, labels=labels, colors=colors,
                startangle=180)

    plt.title(title)
    plt.tight_layout()

    plt.show()


def plot_bar_graph(
        x_axis_data: list, y_axis_data: list,
        x_label: str, y_label: str,  title: str,
        x_ticks_rotation: int | str = 'horizontal', y_ticks_rotation: int | str = 'horizontal',
        x_formatter: str | None = None, y_formatter: str | None = None,
        color_map: str | None = None
) -> None:
    """Plots a bar graph."""
    colors = generate_colors(len(x_axis_data), color_map)

    plt.bar(x_axis_data, y_axis_data, color=colors)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(rotation=x_ticks_rotation)
    plt.yticks(rotation=y_ticks_rotation)
    plt.title(title)
    plt.tight_layout()

    ax = plt.gca()
    if x_formatter:
        ax.xaxis.set_major_formatter(x_formatter)
    if y_formatter:
        ax.yaxis.set_major_formatter(y_formatter)

    plt.show()


def plot_barh_graph(
        x_axis_data: list, y_axis_data: list,
        x_label: str, y_label: str, title: str,
        x_ticks_rotation: int | str = 'horizontal', y_ticks_rotation: int | str = 'horizontal',
        x_formatter: str | None = None, y_formatter: str | None = None,
        color_map: str | None = None
) -> None:
    """Plots a horizontal bar graph."""
    x_axis_data = x_axis_data[::-1]
    y_axis_data = y_axis_data[::-1]

    colors = generate_colors(len(y_axis_data), color_map)

    plt.barh(y_axis_data, x_axis_data, color=colors)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(rotation=x_ticks_rotation)
    plt.yticks(rotation=y_ticks_rotation)
    plt.title(title)
    plt.tight_layout()

    ax = plt.gca()
    if x_formatter:
        ax.xaxis.set_major_formatter(x_formatter)
    if y_formatter:
        ax.yaxis.set_major_formatter(y_formatter)

    plt.show()


def generate_colors(
        color_count: int, color_map: str | None = None
) -> list:
    """Generate a bunch of colors from a given color map."""
    if color_map is None:
        color_map = DEFAULT_COLOR_MAP_GENERATIVE

    cmap = cm.get_cmap(color_map)
    colors = list(cmap(np.linspace(0, 1, color_count)))

    random.shuffle(colors)

    return colors
