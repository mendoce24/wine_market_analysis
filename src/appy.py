import sqlite3
import pandas as pd
import plotly.express as px
import streamlit as st




# Connect to the SQLite database
conn = sqlite3.connect(r'C:\Users\samve\OneDrive\0BeCode\repos\wine_market_analysis\data\vivino.db')
cursor = conn.cursor()
# Query functions
def query_highlight_10_wines():
    query = """
    SELECT v.id, v.name AS vintage_name, v.ratings_average, v.year, v.price_euros, v.ratings_count, w.url
    FROM vintages AS v
    JOIN wines AS w ON v.wine_id = w.id
    JOIN regions AS r ON w.region_id = r.id
    WHERE (v.ratings_average >= 4.4 AND v.price_euros < 20) OR (v.ratings_average >= 4.4 AND v.price_euros BETWEEN 20 AND 50 AND v.ratings_count > 1000 AND v.year != 'N.V.')
    ORDER BY v.year DESC
    LIMIT 10;
    """
    return conn.execute(query).fetchall()

def query_wines_with_taste_keywords():
    query = """
    SELECT w.name, (kw.group_name || '(' || k.name || ')') as group_name, sum(kw.count) 
    FROM wines w
    JOIN keywords_wine kw ON kw.wine_id = w.id
    JOIN keywords k ON k.id = kw.keyword_id
    WHERE w.id in (
        SELECT
            w.id
            FROM wines w
            JOIN keywords_wine kw ON kw.wine_id = w.id
            JOIN keywords k ON k.id = kw.keyword_id
            WHERE k.name in ('coffee','toast','green apple','cream','citrus')
            and kw.count > 10
            and kw.keyword_type = 'primary'
            GROUP BY w.id
            HAVING MAX(CASE WHEN k.name = 'coffee' THEN kw.group_name ELSE 0 END) <> 0 AND 
                MAX(CASE WHEN k.name = 'toast' THEN kw.group_name ELSE 0 END) <> 0 AND 
                MAX(CASE WHEN k.name = 'green apple' THEN kw.group_name ELSE 0 END) <> 0 AND 
                MAX(CASE WHEN k.name = 'cream' THEN kw.group_name ELSE 0 END) <> 0 AND 
                MAX(CASE WHEN k.name = 'citrus' THEN kw.group_name ELSE 0 END) <> 0
            ) and k.name in ('coffee','toast','green apple','cream','citrus')
                and kw.count > 10
                and kw.keyword_type = 'primary'
            GROUP BY w.name, kw.group_name
            ;
    """
    return conn.execute(query).fetchall()

def query_top5_wines_per_grape():
    query = """
    SELECT * FROM 
            (SELECT w.name, w.ratings_average, w.ratings_count, g.name
            FROM wines w
            JOIN regions r ON r.id = w.region_id
            JOIN countries c ON c.code = r.country_code
            JOIN most_used_grapes_per_country mg ON mg.country_code = c.code
            JOIN grapes g ON mg.grape_id = g.id
            WHERE mg.grape_id = 2 and w.ratings_count > 2000
            ORDER BY w.ratings_average DESC, w.ratings_count DESC
            LIMIT 5)

            UNION ALL

            SELECT * FROM 
            (SELECT w.name, w.ratings_average, w.ratings_count, g.name
            FROM wines w
            JOIN regions r ON r.id = w.region_id
            JOIN countries c ON c.code = r.country_code
            JOIN most_used_grapes_per_country mg ON mg.country_code = c.code
            JOIN grapes g ON mg.grape_id = g.id
            WHERE mg.grape_id = 5 and w.ratings_count > 2000
            ORDER BY w.ratings_average DESC, w.ratings_count DESC
            LIMIT 5) 

            UNION ALL

            SELECT * FROM 
            (SELECT w.name, w.ratings_average, w.ratings_count, g.name
            FROM wines w
            JOIN regions r ON r.id = w.region_id
            JOIN countries c ON c.code = r.country_code
            JOIN most_used_grapes_per_country mg ON mg.country_code = c.code
            JOIN grapes g ON mg.grape_id = g.id
            WHERE mg.grape_id = 10 and w.ratings_count > 2000
            ORDER BY w.ratings_average DESC, w.ratings_count DESC
            LIMIT 5)
            ;
    """
    return conn.execute(query).fetchall()

def query_top5_wines_cabernet_sauvignon():
    query = """
    SELECT w.name, w.ratings_average, w.ratings_count, g.name
            FROM wines w
            JOIN regions r ON r.id = w.region_id
            JOIN countries c ON c.code = r.country_code
            JOIN most_used_grapes_per_country mg ON mg.country_code = c.code
            JOIN grapes g ON mg.grape_id = g.id
            WHERE mg.grape_id = 2 and w.ratings_count > 2000
            ORDER BY w.ratings_average DESC, w.ratings_count DESC
            LIMIT 5
            ;
    """
    return conn.execute(query).fetchall()



# Streamlit app
def main():
    st.set_page_config(page_title='Vivino market analysis', page_icon=':fire:', layout='wide')
    st.title("Vivino market analysis")
    st.subheader('By César, Fré and Sam')
    # Select query
    query_option = st.selectbox("Select Query", ["Highlight 10 wines", "Wines with taste keywords", "Top 5 wines for top 3 grapes", "Top 5 wines with Cabernet Sauvignon"])
    
    if query_option == "Highlight 10 wines":
        result = query_highlight_10_wines()
        # Convert the result to a DataFrame
        columns = ['id', 'vintage_name', 'ratings_average', 'year', 'price_euros', 'ratings_count', 'url']
        df = pd.DataFrame(result, columns=columns)
        st.write('# This plot shows the selection of 10 wines to highlight to increase sales.')
        # Create a Plotly visualization
        fig = px.bar(df, x='vintage_name', y='ratings_average', title=f'Best 10 wines to increas sales: {query_option}')
        st.plotly_chart(fig)
    elif query_option == "Wines with taste keywords":
        result = query_wines_with_taste_keywords()
         # Convert the result to a DataFrame
        columns = ['name_wine', 'group_name', 'count']
        df = pd.DataFrame(result, columns=columns)
        fig1 = px.histogram(df, x="name_wine", y="count", color="group_name", marginal="rug",
                   hover_data=df.columns)
        #Plotting the chart
        st.plotly_chart(fig1, use_container_width=True)
    elif query_option == "Top 5 wines for top 3 grapes":
        result = query_top5_wines_per_grape()
         # Convert the result to a DataFrame
        columns = ['wine', 'ratings_average', 'ratings_count', 'grape']
        df = pd.DataFrame(result, columns=columns)
        fig2 = px.histogram(df, x="wine", y="ratings_average", color="grape", marginal="rug",
                   hover_data=df.columns, histfunc='avg')
        #Plotting the chart
        st.plotly_chart(fig2, use_container_width=True)
    elif query_option == "Top 5 wines with Cabernet Sauvignon":
        result = query_top5_wines_cabernet_sauvignon()
         # Convert the result to a DataFrame
        columns = ['wine', 'ratings_average', 'ratings_count', 'grape']
        df = pd.DataFrame(result, columns=columns)
        fig4 = px.histogram(df, x="wine", y="ratings_average", color="grape", marginal="rug",
                   hover_data=df.columns)
        #Plotting the chart
        st.plotly_chart(fig4, use_container_width=True)



# Close the database connection
#conn.close()

if __name__ == '__main__':
    main()
