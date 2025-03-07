import warnings

import mysql.connector

import constants
import section_1
import section_2
import section_3
import section_4

warnings.filterwarnings('ignore')


def main() -> None:
    """Executes and visualizes all queries"""
    conn = mysql.connector.connect(
        host=constants.DB_HOST,
        user=constants.DB_USER,
        password=constants.DB_PASSWORD,
        database=constants.DB_NAME
    )

    if conn.is_connected():
        print("Connection established")

    section_1.all_queries(conn)
    section_2.all_queries(conn)
    section_3.all_queries(conn)
    section_4.all_queries(conn)


if __name__ == "__main__":
    main()
