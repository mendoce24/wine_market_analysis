import sqlite3
import pandas as pd
import plotly.express as px
import streamlit as st

# Connect to the SQLite database
conn = sqlite3.connect(r'C:\Users\samve\OneDrive\0BeCode\repos\wine_market_analysis\data\vivino.db')
cursor = conn.cursor()
# Query functions
def query_top_ratings():
    query = """
    SELECT v.id, v.name, v.ratings_average, v.ratings_count, w.name AS wine_name
    FROM vintages AS v
    JOIN wines AS w ON v.wine_id = w.id
    ORDER BY v.ratings_average DESC, v.ratings_count DESC
    LIMIT 10;
    """
    return conn.execute(query).fetchall()

def query_high_sales():
    query = """
    SELECT v.id, v.name, v.price_euros, v.ratings_count, w.name AS wine_name
    FROM vintages AS v
    JOIN wines AS w ON v.wine_id = w.id
    ORDER BY v.price_euros DESC, v.ratings_count DESC
    LIMIT 10;
    """
    return conn.execute(query).fetchall()

def query_limited_availability():
    query = """
    SELECT v.id, v.name, v.ratings_count, w.name AS wine_name
    FROM vintages AS v
    JOIN wines AS w ON v.wine_id = w.id
    WHERE v.ratings_count < 100
    ORDER BY v.ratings_count ASC
    LIMIT 10;
    """
    return conn.execute(query).fetchall()

def query_trending():
    query = """
    SELECT v.id, v.name, v.ratings_count, w.name AS wine_name
    FROM vintages AS v
    JOIN wines AS w ON v.wine_id = w.id
    WHERE v.ratings_count > 1000
    ORDER BY v.ratings_count DESC
    LIMIT 10;
    """
    return conn.execute(query).fetchall()



# Streamlit app
def main():
    st.title("Top Vintages Analysis")
    
    # Select query
    query_option = st.selectbox("Select Query", ["Top Ratings", "High Sales", "Limited Availability", "Trending"])
    
    if query_option == "Top Ratings":
        result = query_top_ratings()
    elif query_option == "High Sales":
        result = query_high_sales()
    elif query_option == "Limited Availability":
        result = query_limited_availability()
    elif query_option == "Trending":
        result = query_trending()

    # Convert the result to a DataFrame
    columns = ['id', 'name', 'ratings_average', 'ratings_count', 'wine_name']
    df = pd.DataFrame(result, columns=columns)

    # Create a Plotly visualization
    fig = px.bar(df, x='name', y='ratings_average', title=f'Top Vintages: {query_option}')
    st.plotly_chart(fig)
# Close the database connection
#conn.close()

if __name__ == '__main__':
    main()
