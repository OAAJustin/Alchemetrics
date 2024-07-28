from flask import Flask, render_template, request, jsonify
from mysql.connector import Error, cursor, connect
import json

app = Flask(__name__)

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

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

            # Insert data into the MySQL table
            cursor = connection.cursor()
            query = """
                INSERT INTO Inventory (Title, Medium, Size, Qty, Price, Artist)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            
            cursor.execute(query, (title, medium, size, qty, price, artist))
            connection.commit()
        
        return jsonify({'status': 'success', 'message': 'Item added and datbase connected!'}), 200


    except Error as e:
        print("Error while connecting to MySQL", e)
        return jsonify({'status': 'error', 'message': str(e)}), 500
        
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
      
if __name__ == '__main__':
    app.run(debug = True)