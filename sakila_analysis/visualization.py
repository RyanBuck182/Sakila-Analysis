import random
import warnings
from typing import Optional

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

warnings.filterwarnings('ignore')

DEFAULT_COLOR_MAP = 'viridis'
DEFAULT_COLOR_MAP_GENERATIVE = 'turbo'

DOT_PLOT_SCALER = 100000


def plot_pie_chart(
        data: list, labels: list, title: str,
        percents: bool = False, color_map: Optional[str] = None,
        background: Optional[bool] = None
) -> None:
    """Plots a pie chart."""
    data = data[::-1]
    labels = labels[::-1]

    # Generate colors
    colors = generate_colors(len(labels), color_map)

    # Plot data
    _, _, plt_labels = plt.pie(
        data, labels=labels, colors=colors, startangle=180,
        pctdistance=0.75, autopct='%1.2f%%' if percents else '')

    plt.title(title)

    for i, label in enumerate(plt_labels[::-1]):
        if not percents:
            label.set_text(data[i])
        if background:
            label.set_bbox(dict(facecolor='white', edgecolor='black'))

    # Display plot
    plt.tight_layout()
    plt.show()


def plot_bar_graph(
        data: list, labels: list,
        data_label: str, labels_label: str,  title: str,
        x_ticks_rotation: int | str = 'horizontal',
        y_ticks_rotation: int | str = 'horizontal',
        x_formatter: Optional[str] = None, y_formatter: Optional[str] = None,
        color_map: Optional[str] = None
) -> None:
    """Plots a bar graph."""
    # Generate colors
    colors = generate_colors(len(data), color_map)

    # Plot data
    plt.bar(labels, data, color=colors)
    plt.xlabel(labels_label)
    plt.ylabel(data_label)
    plt.xticks(rotation=x_ticks_rotation)
    plt.yticks(rotation=y_ticks_rotation)
    plt.title(title)

    ax = plt.gca()
    if x_formatter:
        ax.xaxis.set_major_formatter(x_formatter)
    if y_formatter:
        ax.yaxis.set_major_formatter(y_formatter)

    # Display plot
    plt.tight_layout()
    plt.show()


def plot_barh_graph(
        data: list, labels: list,
        data_label: str, labels_label: str, title: str,
        x_ticks_rotation: int | str = 'horizontal',
        y_ticks_rotation: int | str = 'horizontal',
        x_formatter: Optional[str] = None, y_formatter: Optional[str] = None,
        color_map: Optional[str] = None
) -> None:
    """Plots a horizontal bar graph."""
    data = data[::-1]
    labels = labels[::-1]

    # Generate colors
    colors = generate_colors(len(labels), color_map)

    # Plot data
    plt.barh(labels, data, color=colors)
    plt.xlabel(data_label)
    plt.ylabel(labels_label)
    plt.xticks(rotation=x_ticks_rotation)
    plt.yticks(rotation=y_ticks_rotation)
    plt.title(title)

    ax = plt.gca()
    if x_formatter:
        ax.xaxis.set_major_formatter(x_formatter)
    if y_formatter:
        ax.yaxis.set_major_formatter(y_formatter)

    # Display plot
    plt.tight_layout()
    plt.show()


def plot_dot_plot(
        x_axis_data: list, y_axis_data: list, step: float,
        x_label: str, y_label: str, title: str,
        x_ticks_rotation: int | str = 'horizontal',
        y_ticks_rotation: int | str = 'horizontal',
        x_formatter: Optional[str] = None, y_formatter: Optional[str] = None,
        color_map: Optional[str] = None
) -> None:
    """Plots a dot plot."""
    # Generate colors
    colors = generate_colors(len(x_axis_data), color_map)

    # Create dot arrays
    dot_colors = []
    x_dots = []
    y_dots = []
    for x, y, color in zip(x_axis_data, y_axis_data, colors):
        # Calculate dot positions
        dots = [dot / DOT_PLOT_SCALER
                for dot in range(0, int(y * DOT_PLOT_SCALER),
                                 int(step * DOT_PLOT_SCALER))]

        # Add dots to arrays
        y_dots.extend(dots)
        x_dots.extend([x] * len(dots))
        dot_colors.extend([color] * len(dots))

    # Plot dots
    plt.scatter(x_dots, y_dots, c=dot_colors)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(rotation=x_ticks_rotation)
    plt.yticks(rotation=y_ticks_rotation)
    plt.title(title)

    ax = plt.gca()
    if x_formatter:
        ax.xaxis.set_major_formatter(x_formatter)
    if y_formatter:
        ax.yaxis.set_major_formatter(y_formatter)

    # Display plot
    plt.tight_layout()
    plt.show()


def plot_doth_plot(
        x_axis_data: list, y_axis_data: list, step: float,
        x_label: str, y_label: str, title: str,
        x_ticks_rotation: int | str = 'horizontal',
        y_ticks_rotation: int | str = 'horizontal',
        x_formatter: Optional[str] = None, y_formatter: Optional[str] = None,
        color_map: Optional[str] = None
) -> None:
    """Plots a horizontal dot plot."""
    x_axis_data = x_axis_data[::-1]
    y_axis_data = y_axis_data[::-1]

    # Generate colors
    colors = generate_colors(len(y_axis_data), color_map)

    # Create dot arrays
    dot_colors = []
    x_dots = []
    y_dots = []
    for x, y, color in zip(x_axis_data, y_axis_data, colors):
        # Calculate dot positions
        dots = [dot / DOT_PLOT_SCALER
                for dot in range(0, int(x * DOT_PLOT_SCALER),
                                 int(step * DOT_PLOT_SCALER))]

        # Add dots to arrays
        x_dots.extend(dots)
        y_dots.extend([y] * len(dots))
        dot_colors.extend([color] * len(dots))

    # Plot dots
    plt.scatter(x_dots, y_dots, c=dot_colors)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(rotation=x_ticks_rotation)
    plt.yticks(rotation=y_ticks_rotation)
    plt.title(title)

    ax = plt.gca()
    if x_formatter:
        ax.xaxis.set_major_formatter(x_formatter)
    if y_formatter:
        ax.yaxis.set_major_formatter(y_formatter)

    # Display plot
    plt.tight_layout()
    plt.show()


def plot_box_plot(
        data: list, data_label: str, title: str,
        x_formatter: Optional[str] = None, y_formatter: Optional[str] = None,
) -> None:
    """Plots a box plot."""
    # Plot data
    bplot = plt.boxplot(data)  # tick_labels=labels
    plt.xlabel(data_label)
    plt.xticks([])
    plt.title(title)

    ax = plt.gca()
    if x_formatter:
        ax.xaxis.set_major_formatter(x_formatter)
    if y_formatter:
        ax.yaxis.set_major_formatter(y_formatter)

    # Display plot
    plt.tight_layout()
    plt.show()


def generate_colors(
        color_count: int, color_map: Optional[str] = None
) -> list:
    """Generate a bunch of colors from a given color map."""
    if color_map is None:
        color_map = DEFAULT_COLOR_MAP_GENERATIVE

    cmap = cm.get_cmap(color_map)
    colors = list(cmap(np.linspace(0, 1, color_count)))

    random.shuffle(colors)

    return colors
