import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# File Name
file_name = 'inventory_6.30.2023.csv'

column_list = (0, 1, 3, 4, 6, 8, 26)

# Read the CSV file
inventory = pd.read_csv(file_name, usecols = column_list)

# Enumerate dataframe columns function
def enum_columns(dataframe_columns):
    for index, column in enumerate(dataframe_columns):
        print(index, column)
        
# List of column names and their data types
# Column Datatypes Function
def column_datatypes(dataframe):
    for column_name, dtype in dataframe.dtypes.items():
        print(f'Column: {column_name}, Data Type: {dtype}')
        
# Categories - A = Aluminum, C = Copper, S = Steel, B = Brass, N = Nickel, T = Titanium
        
# Total Inventory in Pounds
total_inventory_lbs = round(sum(inventory['Qty in Stock']))

# Aluminum Data Frame
aluminum = inventory[inventory['Category'] == 'A']
aluminum_total = round(sum(aluminum['Qty in Stock']))

# Copper Data Frame
copper = inventory[inventory['Category'] == 'C']
copper_total = round(sum(copper['Qty in Stock']))

# Steel Data Frame
steel = inventory[inventory['Category'] == 'S']
steel_total = round(sum(steel['Qty in Stock']))

# Brass Data Frame
brass = inventory[inventory['Category'] == 'B']
brass_total = round(sum(brass['Qty in Stock']))

# Nickel Data Frame
nickel = inventory[inventory['Category'] == 'N']
nickel_total = round(sum(nickel['Qty in Stock']))

# Titanium Data Frame
titanium = inventory[inventory['Category'] == 'T']
titanium_total = round(sum(titanium['Qty in Stock']))

# List of Categories with weights
categories = {'Aluminum': aluminum_total, 'Copper': copper_total, 'Steel': steel_total, 
               'Brass': brass_total, 'Nickel': nickel_total, 'Titanium': titanium_total}

# Category Weights
category_weights = [aluminum_total, copper_total, steel_total, brass_total, nickel_total, titanium_total]

# List of Category names
category_names = ['Aluminum', 'Copper', 'Steel', 'Brass', 'Nickel', 'Titanium']

# Theme for the plot
plt.style.use('fivethirtyeight')

# Figure and Axes Objects
# figsize = (10, 6)
fig, ax = plt.subplots()

# Colors list
colors = ['red', 'green', 'blue', 'orange', 'purple', 'brown']


# Bar Plot of Inventory Totals
plt.bar(categories.keys(), 
        categories.values(),
        color = colors)

# Add labels to each bar
for index, values in enumerate(category_weights):
    plt.text(index, values + 1, str(values), ha='center', va='bottom')

# Format y axis
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: '{:,.0f}'.format(x)))

# Add Legend
ax.legend()

# Show the plot
plt.show()

