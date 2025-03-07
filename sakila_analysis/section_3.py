import mysql.connector
import pandas as pd

import visualization as vis
import constants


def all_queries(conn):
    """Perform all queries and their visualizations."""
    # Uncomment the following when the functions are implemented
    rentals_per_actor(conn)
    rentals_per_sports_actor(conn)
    top_ten_actors_by_rentals(conn)


def rentals_per_actor(conn):
    """3.1: Gets every actor and their total rentals."""
    # Formulate query
    query = """
    SELECT first_name, last_name, COUNT(rental_id) as total_rentals
    FROM actor a
    -- actor to film actor to inventory to rental
    JOIN film_actor fa ON a.actor_id = fa.actor_id
    JOIN inventory i ON i.film_id = fa.film_id
    JOIN rental r ON r.inventory_id = i.inventory_id
    GROUP BY a.actor_id
    LIMIT 50;
    """

    # Perform query on database and store result
    data = pd.read_sql(query, conn)

    # Visualize data
    vis.plot_bar_graph(
        data=data['total_rentals'],
        labels=data['last_name'],
        data_label='Total Rentals',
        labels_label='Actor Name',
        title='3.1 Total Rentals By Actor - Sakila',
        x_ticks_rotation='vertical',
        color_gen=False,
        fig_size=(10, 6)
    )


def rentals_per_sports_actor(conn):
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
    GROUP BY a.actor_id
    LIMIT 45;
    """

    # Perform query on database and store result
    data = pd.read_sql(query, conn)

    # Visualize data
    vis.plot_bar_graph(
        data=data['total_rentals'],
        labels=data['last_name'],
        data_label='Total Rentals',
        labels_label='Actor Name',
        title='3.2 Total Rentals By Actor For Sports Films - Sakila',
        x_ticks_rotation='vertical',
        color_gen=False,
        fig_size=(10, 6)
    )


def top_ten_actors_by_rentals(conn):
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
    vis.plot_bar_graph(
        data=data['total_rentals'],
        labels=data['last_name'],
        data_label='Total Rentals',
        labels_label='Actor Name',
        title='3.3 Top 10 Highest Rental Count - Sakila',
        x_ticks_rotation=45,
        color_gen=False,
        fig_size=(10, 6)
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
