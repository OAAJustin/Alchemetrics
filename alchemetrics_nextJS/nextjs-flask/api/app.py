from flask import Flask, request, jsonify
from sqlalchemy import create_engine
import pandas as pd

app = Flask(__name__)

# Create the SQLAlchemy engine using mysql+mysqlconnector or mysql+pymysql
engine = create_engine("mysql+mysqlconnector://administrator:admin@localhost/vicinanza-studios")
# engine = create_engine("mysql+pymysql://administrator:admin@localhost/vicinanza-studios")

@app.route('/add-item', methods=['POST'])
@app.route('/api/data')
def add_item():
    data = request.json
    title = data['Title']
    medium = data['Medium']
    size = data['Size']
    qty = data['Qty']
    price = data['Price']
    artist = data['Artist']

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
    app.run(debug=True)
