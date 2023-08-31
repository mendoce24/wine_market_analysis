import streamlit as st
import sqlite3
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import numpy as np
import scipy


"# VIVINO "

st.write("")


# Connect to SQLite database
conn = sqlite3.connect(r'../data/vivino.db')

# Create a cursor object
cur = conn.cursor()


cur.execute("""
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
            """)

# Put it all to a data frame
sql_data = pd.DataFrame(cur.fetchall(), columns=['name_wine', 'group_name', 'count'])


fig1 = px.histogram(sql_data, x="name_wine", y="count", color="group_name", marginal="rug",
                   hover_data=sql_data.columns)

#Plotting the chart
"## Wines with (coffee, toast, green apple, cream, citrus) keywords"
st.plotly_chart(fig1, use_container_width=True)




cur.execute("""
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
            """)
sql_dataTotal = pd.DataFrame(cur.fetchall(), columns=['wine', 'ratings_average', 'ratings_count', 'grape'])
     

fig2 = px.histogram(sql_dataTotal, x="wine", y="ratings_average", color="grape", marginal="rug",
                   hover_data=sql_dataTotal.columns, histfunc='avg')

#Plotting the chart
"## Top 5 wines per grapes (Cabernet Sauvignon, Merlot, Chardonnay) "
st.plotly_chart(fig2, use_container_width=True)

cur.execute("""
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
            """)
sql_data2 = pd.DataFrame(cur.fetchall(), columns=['wine', 'ratings_average', 'ratings_count', 'grape'])


fig4 = px.histogram(sql_data2, x="wine", y="ratings_average", color="grape", marginal="rug",
                   hover_data=sql_data2.columns)

#Plotting the chart
"## Wines with grapes Cabernet Sauvignon"
st.plotly_chart(fig4, use_container_width=True)