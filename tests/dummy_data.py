import sys
from pathlib import Path

root_directory = Path(__file__).parent.parent
sys.path.insert(1, str(root_directory))

from database.database import Database
from logs import *

class DummyData(Database):
    def __init__(self) -> None:
        super().__init__()
        self.create_database()
        
    def insert_dummy_data(self) -> None:
        self.connect_to_database()

        self.cursor.execute("""INSERT INTO account (account_id, username, password, email) 
                            VALUES (55, 'test', 'test', 'test');""")

        self.cursor.execute("""INSERT INTO customer (name, address, cell_phone, account_account_id) 
                            VALUES
                            ('Oliver', 'City of Brazil', 123456789, 55),
                            ('Emma', 'City of Brazil', 123456789, 55),
                            ('Sophia', 'City of Brazil', 123456789, 55),
                            ('Harry', 'City of Brazil', 123456789, 55),
                            ('Oscar', 'City of Brazil', 123456789, 55),
                            ('Abigail', 'City of Brazil', 123456789, 55),
                            ('John', 'City of Brazil', 123456789, 55),
                            ('Alice', 'City of Brazil', 123456789, 55),
                            ('Ava', 'City of Brazil', 123456789, 55),
                            ('Ella', 'City of Brazil', 123456789, 55),
                            ('Benjamin', 'City of Brazil', 123456789, 55),
                            ('Charlotte', 'City of Brazil', 123456789, 55),
                            ('Michael', 'City of Brazil', 123456789, 55),
                            ('Amelia', 'City of Brazil', 123456789, 55),
                            ('Daniel', 'City of Brazil', 123456789, 55),
                            ('Mia', 'City of Brazil', 123456789, 55),
                            ('Henry', 'City of Brazil', 123456789, 55),
                            ('Grace', 'City of Brazil', 123456789, 55),
                            ('Alexander', 'City of Brazil', 123456789, 55),
                            ('Liam', 'City of Brazil', 123456789, 55),
                            ('Avery', 'City of Brazil', 123456789, 55),
                            ('Olivia', 'City of Brazil', 123456789, 55),
                            ('Logan', 'City of Brazil', 123456789, 55),
                            ('Evelyn', 'City of Brazil', 123456789, 55),
                            ('Jayden', 'City of Brazil', 123456789, 55),
                            ('Penelope', 'City of Brazil', 123456789, 55),
                            ('Mason', 'City of Brazil', 123456789, 55),
                            ('Madison', 'City of Brazil', 123456789, 55),
                            ('Carter', 'City of Brazil', 123456789, 55),
                            ('Chloe', 'City of Brazil', 123456789, 55)""")
        
        self.cursor.execute("""INSERT INTO category (category_name, description) 
                            VALUES 
                            ('Breakfast', 'nothing'),
                            ('Lunch', 'nothing'),
                            ('Snack', 'nothing'),
                            ('Dinner', 'nothing'),
                            ('Drinks', 'nothing'),
                            ('Vegan', 'nothing'),
                            ('Sweet', 'nothing'),
                            ('Appetizers', 'nothing'),
                            ('Seafood', 'nothing'),
                            ('Pasta', 'nothing'),
                            ('Salads', 'nothing'),
                            ('Desserts', 'nothing'),
                            ('Vegetarian', 'nothing'),
                            ('Beverages', 'nothing'),
                            ('Sides', 'nothing'),
                            ('Soup', 'nothing'),
                            ('Entrees', 'nothing'),
                            ('Cocktails', 'nothing'),
                            ('Steak', 'nothing'),
                            ('Burgers', 'nothing'),
                            ('Pizza', 'nothing'),
                            ('Sushi', 'nothing'),
                            ('Tacos', 'nothing'),
                            ('Wraps', 'nothing'),
                            ('Sandwiches', 'nothing'),
                            ('Dim Sum', 'nothing'),
                            ('Wings', 'nothing'),
                            ('Nachos', 'nothing'),
                            ('BBQ', 'nothing'),
                            ('Ribs', 'nothing'),
                            ('Tapas', 'nothing'),
                            ('Fries', 'nothing')""")

        self.cursor.execute("""INSERT INTO meal (meal_name, sale_price, category_category_id, status) 
                            VALUES 
                            ('Pancakes', 5.99, 1, 'Enabled'),
                            ('Grilled Cheese Sandwich', 6.50, 25, 'Disabled'),
                            ('Apple Pie', 4.50, 12, 'Enabled'),
                            ('Caesar Salad', 7.99, 11, 'Enabled'),
                            ('Lemonade', 1.99, 14, 'Enabled'),
                            ('Vegan Burger', 9.50, 6, 'Enabled'),
                            ('Chocolate Cake', 5.75, 12, 'Enabled'),
                            ('Spring Rolls', 4.25, 8, 'Enabled'),
                            ('Grilled Salmon', 12.99, 9, 'Enabled'),
                            ('Spaghetti Bolognese', 11.50, 10, 'Enabled'),
                            ('Greek Salad', 6.99, 11, 'Enabled'),
                            ('Ice Cream Sundae', 4.99, 12, 'Enabled'),
                            ('Vegetable Stir-fry', 8.75, 13, 'Enabled'),
                            ('Coffee', 2.50, 14, 'Enabled'),
                            ('Garlic Bread', 3.50, 15, 'Enabled'),
                            ('Tomato Soup', 4.99, 16, 'Enabled'),
                            ('Steak Frites', 18.99, 17, 'Enabled'),
                            ('Mojito', 7.50, 18, 'Enabled'),
                            ('Ribeye Steak', 22.50, 19, 'Enabled'),
                            ('BBQ Bacon Burger', 10.99, 20, 'Disabled'),
                            ('Pepperoni Pizza', 12.99, 21, 'Enabled'),
                            ('Sushi Platter', 19.99, 22, 'Enabled'),
                            ('Chicken Tacos', 8.99, 23, 'Enabled'),
                            ('Falafel Wrap', 7.50, 24, 'Enabled'),
                            ('Club Sandwich', 8.99, 25, 'Enabled'),
                            ('Pork Dumplings', 5.99, 26, 'Enabled'),
                            ('Spicy Wings', 9.50, 27, 'Enabled'),
                            ('Loaded Nachos', 11.99, 28, 'Enabled'),
                            ('BBQ Pork Ribs', 16.99, 30, 'Enabled'),
                            ('Tapas Plate', 14.50, 31, 'Disabled'),
                            ('Cheese Fries', 5.75, 32, 'Enabled'),
                            ('Avocado Toast', 6.50, 1, 'Enabled')""")
        
        self.cursor.execute("""INSERT INTO waiter (name, cell_phone) 
                            VALUES 
                            ('Jeferson Santos', 123456789),
                            ('github/devjefersonsantos', 123456789),
                            ('Michael Johnson', 123456789),
                            ('Jennifer Williams', 123456789),
                            ('James Smith', 123456789),
                            ('Lisa Brown', 123456789),
                            ('Robert Jones', 123456789),
                            ('Jessica Davis', 123456789),
                            ('David Miller', 123456789),
                            ('Mary Taylor', 123456789),
                            ('John Anderson', 123456789),
                            ('Lisa Martinez', 123456789),
                            ('Matthew Hernandez', 123456789),
                            ('Jessica Wright', 123456789),
                            ('Daniel Hill', 123456789),
                            ('Susan Scott', 123456789),
                            ('William Green', 123456789),
                            ('Sarah Adams', 123456789),
                            ('Christopher Baker', 123456789),
                            ('Ashley Hall', 123456789),
                            ('Joseph Carter', 123456789),
                            ('Karen Rivera', 123456789),
                            ('Michael Mitchell', 123456789),
                            ('Kimberly Torres', 123456789),
                            ('Christopher Lopez', 123456789),
                            ('Sarah Hill', 123456789),
                            ('Anthony Flores', 123456789),
                            ('Laura King', 123456789),
                            ('Kevin Adams', 123456789),
                            ('Emily Campbell', 123456789),
                            ('Mark Reed', 123456789),
                            ('Melissa Murphy', 123456789)""")

        self.connection.commit()
        self.connection.close()
        self.cursor.close()

if __name__ == "__main__":
    while True:
        question = input("Are you sure you want to add dummy data to the database? [Y/N] ")
        if question.upper() == "Y":
            DummyData().insert_dummy_data()
            log_warning(f"Dummy data inserted into the database.")
            print("Dummy data inserted successfully.")
            break
        elif question.upper() == "N":
            break
