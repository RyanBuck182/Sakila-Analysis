import mysql.connector
import pandas as pd

import visualization as vis
import constants


def all_queries(conn):
    """Perform all queries and their visualizations."""
    # Uncomment the following when the functions are implemented
    # FIRST_QUERY_FUNCTION(conn)
    # SECOND_QUERY_FUNCTION(conn)
    # THIRD_QUERY_FUNCTION(conn)


def FIRST_QUERY_FUNCTION(conn):
    """4.1: DESCRIBE THE QUERY HERE."""
    # Formulate query
    query = """
    YOUR QUERY
    """

    # Perform query on database and store result
    data = pd.read_sql(query, conn)

    # Visualize data
    # CHANGE THE GRAPH TYPE AND SETTINGS
    vis.plot_barh_graph(
        data=data,
        x_axis='rentalCount',
        y_axis='name',
        x_label='Rental Count',
        y_label='Film Category',
        title='2.1 Rental Count By Film Category - Sakila',
        color_dict=vis.generate_colors(data['name'])
    )


def SECOND_QUERY_FUNCTION(conn):
    """4.2: DESCRIBE THE QUERY HERE."""
    # Formulate query
    query = """
    YOUR QUERY
    """

    # Perform query on database and store result
    data = pd.read_sql(query, conn)

    # Visualize data
    # CHANGE THE GRAPH TYPE AND SETTINGS
    vis.plot_barh_graph(
        data=data,
        x_axis='rentalRate',
        y_axis='name',
        x_label='Average Rental Cost Per Day',
        y_label='Film Category',
        title='2.2 Rental Cost By Film Category - Sakila',
        x_formatter="${x:.2f}",
        color_dict=vis.generate_colors(data['name'])
    )


def THIRD_QUERY_FUNCTION(conn):
    """4.3: DESCRIBE THE QUERY HERE."""
    # Formulate query
    query = """
    YOUR QUERY
    """

    # Perform query on database and store result
    data = pd.read_sql(query, conn)

    # Visualize data
    # CHANGE THE GRAPH TYPE AND SETTINGS
    vis.plot_barh_graph(
        data=data,
        x_axis='rentalCount',
        y_axis='title',
        x_label='Rental Count',
        y_label='Film Title',
        title='2.3 Top 5 Most Rented Sports Films - Sakila',
        color_dict=vis.generate_colors(data['title'])
    )


if __name__ == "__main__":
    db_conn = mysql.connector.connect(
        host=constants.DB_HOST,
        user=constants.DB_USER,
        password=constants.DB_PASSWORD,
        database=constants.DB_NAME
    )

    if db_conn.is_connected():
        print("Connection established")

    all_queries(db_conn)
