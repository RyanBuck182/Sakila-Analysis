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
    """3.1: Gets every actor and their total rentals."""
    # Formulate query
    query = """
    SELECT first_name, last_name, COUNT(rental_id) as total_rentals
    FROM actor a
    JOIN film_actor fa ON a.actor_id = fa.actor_id
    JOIN inventory i ON i.film_id = fa.film_id
    JOIN rental r ON r.inventory_id = i.inventory_id
    GROUP BY a.actor_id;
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
    """3.2: Gets the rentals for every actor in sports."""
    # Formulate query
    query = """
    SELECT first_name, last_name, COUNT(rental_id) as total_rentals, c.name
    FROM actor a
    JOIN film_actor fa ON a.actor_id = fa.actor_id
    JOIN inventory i ON i.film_id = fa.film_id
    JOIN rental r ON r.inventory_id = i.inventory_id
    JOIN film_category fc ON fc.film_id = fa.film_id
    JOIN category c ON c.category_id = fc.category_id
    WHERE c.name = "Sports"
    GROUP BY a.actor_id;
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
    """3.3: Gets the top 10 actors with most rentals."""
    # Formulate query
    query = """
    SELECT first_name, last_name, COUNT(rental_id) as total_rentals
    FROM actor a
    JOIN film_actor fa ON a.actor_id = fa.actor_id
    JOIN inventory i ON i.film_id = fa.film_id
    JOIN rental r ON r.inventory_id = i.inventory_id
    GROUP BY a.actor_id
    ORDER BY total_rentals DESC
    LIMIT 10;
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
    host="localhost",
    user="root",
    password = "toastysnail8561+",
    database = "sakila"
    )

    if db_conn.is_connected():
        print("Connection established")

    all_queries(db_conn)
