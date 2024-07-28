from flask import Flask, render_template, request, jsonify
from mysql.connector import Error, cursor, connect
from sqlalchemy import create_engine, text
import json
import pandas as pd

app = Flask(__name__)

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

engine = create_engine(f"mysql+mysqlconnector://{config['user']}:{config['password']}@{config['host']}/{config['database']}")

@app.route('/add-item', methods=['POST'])
def add_item():
    data = request.json
    title = data['Title']
    medium = data['Medium']
    size = data['Size']
    qty = data['Qty']
    price = data['Price']
    artist = data['Artist']

    try:
        # Establish the connection
        connection = connect(
            host=config['host'],
            user=config['user'],
            password=config['password'],
            database=config['database'],
        )

        if connection.is_connected():
            print('Connected to the database')

            # Your SQL operations go here
            # For example, creating a cursor and executing a query

        # Insert data into the MySQL table
        with engine.connect() as connection:
            query = text(f"""
                INSERT INTO Inventory (Title, Medium, Size, Qty, Price, Artist)
                VALUES (title, medium, size, qty, price, artist)
            """)
            connection.execute(query, title=title, medium=medium, size=size, qty=qty, price=price, artist=artist)
        
        return jsonify({'status': 'success', 'message': 'Item added and datbase connected!'}), 200


    except Error as e:
        print("Error while connecting to MySQL", e)
        return jsonify({'status': 'error', 'message': str(e)}), 500
        
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True, port = 3000)