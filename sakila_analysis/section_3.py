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
    """3.1: DESCRIBE THE QUERY HERE."""
    # Formulate query
    query = """
    YOUR QUERY
    """

    # Perform query on database and store result
    data = pd.read_sql(query, conn)

    # Visualize data
    # CHANGE THE GRAPH TYPE AND SETTINGS
    vis.plot_barh_graph(
        data=data['placeholderColumnName'],
        labels=data['placeholderColumnName'],
        data_label='Placeholder X Label',
        labels_label='Placeholder Y Label',
        title='X.X Placeholder Title - Sakila',
    )


def SECOND_QUERY_FUNCTION(conn):
    """3.2: DESCRIBE THE QUERY HERE."""
    # Formulate query
    query = """
    YOUR QUERY
    """

    # Perform query on database and store result
    data = pd.read_sql(query, conn)

    # Visualize data
    # CHANGE THE GRAPH TYPE AND SETTINGS
    vis.plot_barh_graph(
        data=data['placeholderColumnName'],
        labels=data['placeholderColumnName'],
        data_label='Placeholder X Label',
        labels_label='Placeholder Y Label',
        title='X.X Placeholder Title - Sakila',
    )


def THIRD_QUERY_FUNCTION(conn):
    """3.3: DESCRIBE THE QUERY HERE."""
    # Formulate query
    query = """
    YOUR QUERY
    """

    # Perform query on database and store result
    data = pd.read_sql(query, conn)

    # Visualize data
    # CHANGE THE GRAPH TYPE AND SETTINGS
    vis.plot_barh_graph(
        data=data['placeholderColumnName'],
        labels=data['placeholderColumnName'],
        data_label='Placeholder X Label',
        labels_label='Placeholder Y Label',
        title='X.X Placeholder Title - Sakila',
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
