import sqlite3
import pandas as pd
import plotly.express as px
import streamlit as st
# Connect to SQLite database
conn = sqlite3.connect(r'C:\Users\samve\OneDrive\0BeCode\repos\wine_market_analysis\data\vivino.db')

# Create a cursor object
cur = conn.cursor()

cur.execute("""
    SELECT
        vintages.ratings_average,
        vintages.ratings_count,
        vintages.name,
        vintages.price_euros
    FROM
        vintages
    WHERE
        vintages.price_euros BETWEEN 20 AND 30
    ORDER BY
        vintages.ratings_average DESC,
        vintages.ratings_count DESC;
""")

# Fetch the query result
query_result = cur.fetchall()

# Create a DataFrame from the query result
df = pd.DataFrame(query_result, columns=['ratings_average', 'ratings_count', 'name', 'price_euros'])

# Close the database connection
conn.close()

# Create a scatter plot using Plotly Express
scatter_plot = px.scatter(df, x='ratings_average', y='ratings_count', 
                          color='price_euros', color_continuous_scale='Viridis',
                          size='price_euros', hover_name='name', title='Wine Ratings')
scatter_plot.show()
st.plotly_chart(scatter_plot)