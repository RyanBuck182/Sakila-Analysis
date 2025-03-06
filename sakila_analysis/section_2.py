import mysql.connector
import pandas as pd

import visualization as vis
import constants


def all_queries(conn):
    """Perform all queries and their visualizations."""
    rental_count_by_film_category(conn)
    rental_rate_by_film_category(conn)
    most_rented_sports_films(conn)


def rental_count_by_film_category(conn):
    """2.1: Total rental counts by film category."""
    # Formulate query
    query = """
    SELECT c.name, COUNT(*) as rentalCount
    FROM sakila.rental r
    INNER JOIN sakila.inventory i ON r.inventory_id = i.inventory_id
    INNER JOIN sakila.film_category f ON i.film_id = f.film_id
    INNER JOIN sakila.category c ON f.category_id = c.category_id
    GROUP BY c.name
    ORDER BY rentalCount DESC;
    """

    # Perform query on database and store result
    data = pd.read_sql(query, conn)

    # Visualize data
    vis.plot_barh_graph(
        data=data,
        x_axis='rentalCount',
        y_axis='name',
        x_label='Rental Count',
        y_label='Film Category',
        title='2.1 Rental Count By Film Category - Sakila',
        color_dict=vis.generate_colors(data['name'])
    )


def rental_rate_by_film_category(conn):
    """2.2: Average rental cost by film category."""
    # Formulate query
    query = """
    SELECT c.name, AVG(f.rental_rate / f.rental_duration) AS rentalRate
    FROM sakila.film f
    INNER JOIN sakila.film_category fc ON f.film_id = fc.film_id
    INNER JOIN sakila.category c ON fc.category_id = c.category_id
    GROUP BY c.name
    ORDER BY rentalRate DESC;
    """

    # Perform query on database and store result
    data = pd.read_sql(query, conn)

    # Visualize data
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


def most_rented_sports_films(conn):
    """2.3: Ranking of sports films by rental count."""
    # Formulate query
    query = """
    SELECT f.title, COUNT(*) AS rentalCount
    FROM sakila.rental r
    INNER JOIN sakila.inventory i ON r.inventory_id = i.inventory_id
    INNER JOIN sakila.film f ON i.film_id = f.film_id
    INNER JOIN sakila.film_category fc ON i.film_id = fc.film_id
    INNER JOIN sakila.category c ON fc.category_id = c.category_id
    WHERE c.name = "Sports"
    GROUP BY i.film_id
    ORDER BY rentalCount DESC
    LIMIT 5;
    """

    # Perform query on database and store result
    data = pd.read_sql(query, conn)

    # Visualize data
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
