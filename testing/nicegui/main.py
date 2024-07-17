import os
from nicegui import ui
from mysql.connector import cursor, connect
import json

ui.label('Vicinanza Studios Database')

# Read the JSON file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Database connection details from environment variables
db_config = {
    'host': os.getenv('MYSQL_HOST', {config['localhost']}),
    'port': int(os.getenv('MYSQL_PORT', 3306)),
    'user': os.getenv('MYSQL_USER', {config['user']}),
    'password': os.getenv('MYSQL_PASSWORD', {config['password']}),
    'database': os.getenv('MYSQL_DATABASE', {config['database']})
}

# Define a function to create the form
def show_form():
    with ui.dialog() as dialog, ui.card():
        ui.label('Fill out the form below:')
        ui.input('Name')
        ui.input('Email')
        ui.button('Submit', on_click=dialog.close)

# Create the "Add" button and link it to the show_form function
ui.button('Add', on_click=show_form)

# Run the NiceGUI application
ui.run(port=8000)