import random
import warnings

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

warnings.filterwarnings('ignore')


def generate_colors(qualitative_data: list, color_map: str = 'turbo') -> dict:
    """Generate a color dict based on the given data and a color map.

    Basically you can use this to generate a unique color for every piece of
    qualitative data. Qualitative data is stuff like the title of a film, the
    name of an actor, a category, etc.

    You can pass the returned color dict to a visualization function to set the
    colors of the data in the chart.
    """
    shuffled_data = qualitative_data.copy()
    random.shuffle(shuffled_data)

    viridis = cm.get_cmap(color_map)
    colors = viridis(np.linspace(0, 1, len(shuffled_data)))

    color_dict = {}
    for category, color in zip(shuffled_data, colors):
        color_dict[category] = color

    return color_dict


def plot_barh_graph(
        data: pd.DataFrame, x_axis: str, y_axis: str,
        x_label: str, y_label: str, title: str,
        x_formatter: str | None = None, y_formatter: str | None = None,
        color_dict: dict | None = None
) -> None:
    """Plots a horizontal bar graph."""
    x_axis_data = data[x_axis][::-1]
    y_axis_data = data[y_axis][::-1]

    # Use color dict if available, otherwise use viridis
    if color_dict is None:
        viridis = cm.get_cmap('viridis')
        colors = viridis(np.linspace(0, 1, len(y_axis_data)))
    else:
        colors = []
        for data_point in y_axis_data:
            colors.append(color_dict[data_point])

    plt.barh(y_axis_data, x_axis_data, color=colors)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.tight_layout()

    ax = plt.gca()
    if x_formatter:
        ax.xaxis.set_major_formatter(x_formatter)
    if y_formatter:
        ax.yaxis.set_major_formatter(y_formatter)

    plt.show()
