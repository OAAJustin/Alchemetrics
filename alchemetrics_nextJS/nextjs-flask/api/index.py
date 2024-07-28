from flask import Flask, jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL

app = Flask(__name__)
CORS(app)

# Configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'tarroyo'
app.config['MYSQL_PASSWORD'] = 'Password!'
app.config['MYSQL_DB'] = 'vicinanza-studios'

mysql = MySQL(app)

@app.route("/api/python")
@app.route('/api/data', methods=['GET'])

def get_data():
    cur = mysql.connection.cursor()
    cur.execute("SELECT uid, artist, title, medium, size, qty, price FROM inventory")
    results = cur.fetchall()
    cur.close()

    data = []
    for row in results:
        data.append({
            'uid': row[0],
            'artist': row[1],
            'title': row[2],
            'medium': row[3],
            'size': row[4],
            'qty': row[5],
            'price': row[6],
        })
    
    return jsonify(data)