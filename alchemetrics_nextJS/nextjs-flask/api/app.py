from flask import Flask, request, jsonify
from sqlalchemy import create_engine
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Create the SQLAlchemy engine using mysql+mysqlconnector or mysql+pymysql
engine = create_engine("mysql+mysqlconnector://administrator:admin@localhost/vicinanza-studios")
# engine = create_engine("mysql+pymysql://administrator:admin@localhost/vicinanza-studios")

@app.route('/add-item', methods=['POST'])
@app.route('/api/data')
def add_item():
    title = 'Example Title',
    medium = 'Oil on Canvas',
    size = '24',
    qty = 1,
    price = 200,
    artist = 'John Doe'


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

if __name__ == '__main__':
    app.run(debug=True, port = 8080)
