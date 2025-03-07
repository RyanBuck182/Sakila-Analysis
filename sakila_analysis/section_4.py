import mysql.connector
import pandas as pd

import visualization as vis
import constants


def all_queries(conn):
    """Perform all queries and their visualizations."""
    # Uncomment the following when the functions are implemented
    # FIRST_QUERY_FUNCTION(conn)
    payment_per_rental(conn)
    # monthly_revenue(conn)


def revenue_by_store(conn):
    """4.1: DESCRIBE THE QUERY HERE."""
    # Formulate query
    query = """
    SELECT c.city AS store, SUM(p.amount) AS revenue
    FROM sakila.payment p
    JOIN sakila.staff stf ON p.staff_id = stf.staff_id
    JOIN sakila.store str ON stf.store_id = str.store_id
    JOIN sakila.address a ON str.address_id = a.address_id
    JOIN sakila.city c ON a.city_id = c.city_id
    GROUP BY str.store_id;
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


def payment_per_rental(conn):
    """4.2: Boxplot of rental payment amounts."""
    # Formulate query
    query = """
    SELECT p.payment_id, p.amount
    FROM sakila.payment p;
    """

    # Perform query on database and store result
    data = pd.read_sql(query, conn)

    # Visualize data
    # CHANGE THE GRAPH TYPE AND SETTINGS
    vis.plot_box_plot(
        data=data['amount'],
        data_label='Payment Amount',
        title='4.2 Rental Payment Amount - Sakila',
        y_formatter="${x:.2f}",
    )


def monthly_revenue(conn):
    """4.3: DESCRIBE THE QUERY HERE."""
    # Formulate query
    query = """
    SELECT MONTH(p.payment_date) AS month, SUM(p.amount) AS revenue
    FROM sakila.payment p
    GROUP BY month
    ORDER BY month ASC;
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
