#!/usr/bin/python3
"""
This script takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa.
"""
import MySQLdb
import os
import argparse


def get_database_connection():
    """Establishes a connection to the database using environment variables."""
    host = os.getenv('DB_HOST', 'localhost')
    port = int(os.getenv('DB_PORT', 3306))
    user = os.getenv('DB_USER')
    passwd = os.getenv('DB_PASS')
    db_name = os.getenv('DB_NAME')

    return MySQLdb.connect(
        host=host, port=port, user=user, passwd=passwd, db=db_name
    )


def get_cities_by_state(cursor, state_name):
    """Fetches cities for the given state name."""
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id;
    """
    cursor.execute(query, (state_name,))
    return [row[0] for row in cursor.fetchall()]


def main(state_name):
    """Main function to fetch and print cities of the specified state."""
    db = get_database_connection()
    cursor = db.cursor()

    try:
        cities = get_cities_by_state(cursor, state_name)
        print(', '.join(cities))
    finally:
        cursor.close()
        db.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='List all cities of a given state.'
    )
    parser.add_argument('state_name', type=str, help='Name of the state')

    args = parser.parse_args()
    main(args.state_name)
