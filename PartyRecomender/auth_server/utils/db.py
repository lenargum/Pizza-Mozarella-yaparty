import os

import psycopg2


def open_connection_and_get_cursor():
    conn = psycopg2.connect(user=os.getenv('DB_USER'),
                            password=os.getenv('DB_PASSWORD'),
                            host=os.getenv('DB_HOST'),
                            port=os.getenv('DB_PORT'),
                            database=os.getenv('DB_NAME'),
                            target_session_attrs="read-write",
                            sslmode="verify-full"
                            )
    cursor = conn.cursor()
    return conn, cursor


def commit_transaction_and_close_connection(conn, cursor):
    conn.commit()
    cursor.close()
    conn.close()
