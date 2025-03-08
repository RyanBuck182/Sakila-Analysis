import mysql.connector
import pandas as pd
import visualization as vis
import constants
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap  #for the colour blind

purple_gold = ListedColormap(["#800080", "#FFD700"])

def all_queries(conn):
    """Execute all queries and visualize the results."""
    total_rentals_per_customer(conn)
    average_rental_duration(conn)
    rental_counts_distribution(conn)


def total_rentals_per_customer(conn):
    """1.1: Total rentals per customer."""
    query = """
        SELECT customer_id, COUNT(rental_id) AS RentalCount
        FROM sakila.rental
        GROUP BY customer_id
        ORDER BY RentalCount DESC;
        """
    data = pd.read_sql(query, conn)
    vis.plot_bar_graph(
        data=data['RentalCount'],
        labels=data['customer_id'],
        data_label='Total Rentals',
        labels_label='Customer ID',
        title='Total Rentals Per Customer - Sakila',
        x_ticks_rotation=45,
        color_map=purple_gold
    )


def average_rental_duration(conn):
    """
    1.2 Average rental duration per customer
    Source: https://www.w3resource.com/mysql/date-and-time-functions/mysql-timestampdiff-function.php
    """
    query = """
        SELECT customer_id, AVG(TIMESTAMPDIFF(MINUTE, rental_date, return_date)) AS avg_duration
        FROM sakila.rental
        WHERE return_date IS NOT NULL
        GROUP BY customer_id
        ORDER BY avg_duration DESC;
    """
    data = pd.read_sql(query, conn)
    plt.figure()
    bp = plt.boxplot(data['avg_duration'], patch_artist=True)
    colors = ["#800080", "#FFD700"]
    for i, box in enumerate(bp['boxes']):
        box.set_facecolor(colors[i % 2])
    plt.xlabel('Average Rental Duration (minutes)')
    plt.title('Average Rental Duration per Customer - Sakila')
    plt.tight_layout()
    plt.show()


def rental_counts_distribution(conn):
    """Distribution of rentals across months"""
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
        title='Distribution of Rental Counts by Month - Sakila',
        color_map=purple_gold
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
