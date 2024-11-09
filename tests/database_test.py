from database.database import Database

def test_connect_to_database():
    database_connection = Database()
    result = database_connection.connect_to_database()
    assert result == True, "No connection"

def test_create_database():
    database_connection = Database()
    try:
        database_connection.create_database()

        database_connection.connect_to_database()
        database_connection.cursor.execute("SELECT * FROM pg_database WHERE datname = 'restaurant_management_system';")

        assert bool(database_connection.cursor.fetchone()), "Database not found"
    finally:
        database_connection.cursor.close()
        database_connection.connection.close()
