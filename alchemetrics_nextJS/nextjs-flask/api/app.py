#region Import 3rd party dependencies
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, text
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

@app.route('/get-data', methods=['GET'])
def get_data():
    # Define the query to fetch the data
    query = "SELECT uid, artist, title, medium, size, qty, price FROM Inventory"
    
    # Fetch the data into a DataFrame
    df = pd.read_sql(query, engine)
    
    # Convert the DataFrame to JSON
    data_json = df.to_json(orient='records')
    
    return jsonify(data_json)

@app.route('/delete-item', methods=['POST'])
def delete_item():
    data = request.json
    
    # Extract the UID from the JSON data
    uid = data.get('UID')
    
    # Query the item from the Inventory table by UID using pandas
    query = f"SELECT * FROM Inventory WHERE UID = '{uid}'"
    item_to_delete = pd.read_sql(query, engine)

    if not item_to_delete.empty:  # Check if the item exists
        item = item_to_delete.iloc[0]  # Get the first (and only) row

        # Convert the item to a DataFrame for easy insertion into the Archive table
        item_df = pd.DataFrame([item])

        # Insert the item into the Archive table
        item_df.to_sql('Archive', con=engine, if_exists='append', index=False)

        # Delete the item from the Inventory table
        delete_query = text(f"DELETE FROM Inventory WHERE UID = 240")
        with engine.connect() as conn:
            # Begin a transaction
            trans = conn.begin()

            try:
                # Insert the item into the Archive table
                item_df.to_sql('Archive', con=engine, if_exists='append', index=False)

                # Delete the item from the Inventory table
                delete_query = text(f"DELETE FROM Inventory WHERE UID = {uid}")
                print(f"Executing query: {delete_query}")  # Log the delete query
                result = conn.execute(delete_query)

                # Check if any rows were deleted
                if result.rowcount == 0:
                    print(f"No rows deleted for UID: {uid}")
                else:
                    print(f"Deleted {result.rowcount} row(s) from Inventory")

                # Commit the transaction
                trans.commit()

                return jsonify({"message": "Item archived and deleted from inventory"}), 200
            
            except Exception as e:
                # Rollback in case of error
                trans.rollback()
                print(f"Error occurred: {e}")
                return jsonify({"message": f"An error occurred: {str(e)}"}), 500
    else:
        return jsonify({"message": "Item not found"}), 404

    
#region When the python program has been called in the command line, it will run whatever is under the :
if __name__ == '__main__':
    app.run(debug=True, port=8080)
#endregion When the python program has been called in the command line, it will run whatever is under the :
