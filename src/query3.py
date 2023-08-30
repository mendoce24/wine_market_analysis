#This query reports the vintage with the best avg rating on more then 100 ratings and a price below 30


import sqlite3
import pandas as pd
import plotly.express as px

# Connect to the SQLite database
conn = sqlite3.connect(r'C:\Users\samve\OneDrive\0BeCode\repos\wine_market_analysis\data\vivino.db')

# Execute the query and fetch data
query = """
SELECT v.name AS vintage_name, v.ratings_average, v.year, v.price_euros, v.ratings_count
FROM vintages AS v
JOIN wines AS w ON v.wine_id = w.id
JOIN regions AS r ON w.region_id = r.id
WHERE v.ratings_average >= 4.5 AND v.price_euros < 30 AND v.ratings_count > 100
ORDER BY v.year DESC
LIMIT 1;
"""
result = conn.execute(query).fetchall()

# Close the database connection
conn.close()

# Convert the result to a Pandas DataFrame
columns = ['vintage_name', 'ratings_average', 'year', 'price_euros', 'ratings_count']
df = pd.DataFrame(result, columns=columns)

# Create a Plotly visualization
fig = px.bar(df, x='vintage_name', y='ratings_average',
             hover_data=['year', 'price_euros', 'ratings_count'],
             title='Most Recent Vintage with Good Rating')
fig.update_layout(xaxis_title='Vintage', yaxis_title='Ratings Average')
fig.show()