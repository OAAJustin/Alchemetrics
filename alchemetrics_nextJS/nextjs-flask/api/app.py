#region Import 3rd party dependencies
from flask import Flask, request, jsonify
from sqlalchemy import create_engine
import pandas as pd
from flask_cors import CORS
#endregion Import 3rd party dependencies

#region Initiate Flask app
app = Flask(__name__)
CORS(app)
#endregion Initiate Flask app

#region Create the SQLAlchemy engine using mysql+mysqlconnector
# Create the SQLAlchemy engine using mysql+mysqlconnector or mysql+pymysql
engine = create_engine("mysql+mysqlconnector://administrator:admin@localhost/vicinanza-studios")
# engine = create_engine("mysql+pymysql://administrator:admin@localhost/vicinanza-studios")
#endregion Create the SQLAlchemy engine using mysql+mysqlconnector

#region Define the add_item function that routes to /add-item 
@app.route('/add-item', methods=['POST']) # Initialize the /add-item method as a POST
@app.route('/api/data')
def add_item(): # Add item function definition
    data = request.json # Information stored inside the data variable for JSON to read and inserted into the variables
    title = data.get('Title') # Title of the art
    medium = data.get('Medium') # The medium that the art was made - i.e. Oil, Acrylic, etc. 
    size = data.get('Size') # Size of the art piece
    qty = data.get('Qty') # Quantity in stock
    price = data.get('Price') # Price of the art piece
    artist = data.get('Artist') # The artist of the piece


    # Create a DataFrame for the new row
    df = pd.DataFrame({
        'Title': [title],
        'Medium': [medium],
        'Size': [size],
        'Qty': [qty],
        'Price': [price],
        'Artist': [artist]
    })

    # Export the DataFrame to the SQL table
    df.to_sql('Inventory', con=engine, if_exists='append', index=False)

    return jsonify({'status': 'success', 'message': 'Item added successfully!'}), 200
#endregion Define the add_item function that routes to /add-item

#region Define the refresh_inventory function that routes to /refresh-inventory 
@app.route('/refresh-inventory', methods=['GET']) # Initialize the /refresh-inventory method as a GET
def refresh_inventory(): # Refresh inventory function definition
    # Query the Inventory table
    query = "SELECT * FROM Inventory"
    inventory_df = pd.read_sql(query, con=engine)

    # Convert the DataFrame to JSON
    inventory_json = inventory_df.to_json(orient='records')

    return jsonify({'status': 'success', 'data': inventory_json}), 200
#endregion Define the refresh_inventory function that routes to /refresh-inventory

@app.route('/get-data', methods=['GET'])
def get_data():
    # Define the query to fetch the data
    query = "SELECT uid, artist, title, medium, size, qty, price FROM Inventory"
    
    # Fetch the data into a DataFrame
    df = pd.read_sql(query, engine)
    
    # Convert the DataFrame to JSON
    data_json = df.to_json(orient='records')
    
    return jsonify(data_json)

#region When the python program has been called in the command line, it will run whatever is under the :
if __name__ == '__main__':
    app.run(debug=True, port=8080)
#endregion When the python program has been called in the command line, it will run whatever is under the :
