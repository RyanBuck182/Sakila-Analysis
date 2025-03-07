import mysql.connector
import pandas as pd

import visualization as vis
import constants


def all_queries(conn):
    """Execute all queries and visualize the results."""
    total_rentals_per_customer(conn)
    average_rental_duration(conn)
    rental_counts_distribution(conn)


def total_rentals_per_customer(conn):
    """ description"""

    query = """
        SELECT customer_id, COUNT(rental_id) AS RentalCount
        FROM sakila.rental
        GROUP BY customer_id
        ORDER BY RentalCount DESC;
    """
    data = pd.read_sql(query, conn)
    vis.plot_barh_graph(
        data=data['RentalCount'],
        labels=data['customer_id'],
        data_label='Total Rentals',
        labels_label='Customer ID',
        title='Total Rentals Per Customer - Sakila',
    )


def average_rental_duration(conn):
    """description
    source:https://www.w3resource.com/mysql/date-and-time-functions/mysql-timestampdiff-function.php
    """
    query = """
        SELECT customer_id, AVG(TIMESTAMPDIFF(MINUTE, rental_date, return_date)) AS avg_duration
        FROM sakila.rental
        WHERE return_date IS NOT NULL
        GROUP BY customer_id
        ORDER BY avg_duration DESC;
    """
    data = pd.read_sql(query, conn)
    vis.plot_barh_graph(
        data=data['avg_duration'],
        labels=data['customer_id'],
        data_label='Avg Duration (minutes)',
        labels_label='Customer ID',
        title='Top 10 Customers by Average Rental Duration - Sakila'
    )


def rental_counts_distribution(conn):
    """ description"""
    query = """
        SELECT MONTH(rental_date) AS month, COUNT(rental_id) AS rental_count
        FROM sakila.rental
        GROUP BY month
        ORDER BY month ASC;
    """
    data = pd.read_sql(query, conn)
    vis.plot_bar_graph(
        data=data['rental_count'],
        labels=data['month'],
        data_label='Number of Rentals',
        labels_label='Month',
        title='Distribution of Rental Counts by Month - Sakila'
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
