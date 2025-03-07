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
        data=data['placeholderColumnName'],
        labels=data['placeholderColumnName'],
        data_label='Placeholder X Label',
        labels_label='Placeholder Y Label',
        title='X.X Placeholder Title - Sakila',
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
        data=data['placeholderColumnName'],
        labels=data['placeholderColumnName'],
        data_label='Placeholder X Label',
        labels_label='Placeholder Y Label',
        title='X.X Placeholder Title - Sakila',
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
        data=data['placeholderColumnName'],
        labels=data['placeholderColumnName'],
        data_label='Placeholder X Label',
        labels_label='Placeholder Y Label',
        title='X.X Placeholder Title - Sakila',
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
