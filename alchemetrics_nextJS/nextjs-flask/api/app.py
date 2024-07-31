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
    artist = 'John Doe'
    title = 'Example Title'
    medium = 'Oil on Canvas'
    size = 24
    qty = 1
    price = 200.0

    # Create a DataFrame for the new row
    df = pd.DataFrame({
        'artist': [artist],
        'title': [title],
        'medium': [medium],
        'size': [size],
        'qty': [qty],
        'price': [price],
    })

    # Export the DataFrame to the SQL table
    print("Dataframe created!")
    df.to_sql('inventory', con=engine, if_exists='append', index=False)
    
    return jsonify({'status': 'success', 'message': 'Item added successfully!'}), 200

if __name__ == '__main__':
    app.run(debug=True, port = 8080)
