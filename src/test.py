import streamlit as st
import sqlite3
import pandas as pd

"# VIVINO "

st.write("")


# Connect to SQLite database
conn = sqlite3.connect(r'../data/vivino.db')

# Create a cursor object
cur = conn.cursor()


cur.execute("""
            SELECT k.name, sum(kw.count) 
            FROM wines w
            JOIN keywords_wine kw ON kw.wine_id = w.id
            JOIN keywords k ON k.id = kw.keyword_id
            WHERE k.name in ('coffee','toast','green apple','cream','citrus')
                and kw.count > 10
                and kw.keyword_type = 'primary'
            GROUP BY k.name
            ;
            """)

# Put it all to a data frame
sql_data = pd.DataFrame(cur.fetchall(), columns=[ 'name_keywords','count'])

st.bar_chart(sql_data,x='name_keywords', y='count', color='name_keywords')