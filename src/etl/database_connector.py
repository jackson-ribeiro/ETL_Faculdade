import psycopg2


def connect_to_db(host, port, database, user, password):
    return psycopg2.connect(
        host=host, port=port, database=database, user=user, password=password
    )
