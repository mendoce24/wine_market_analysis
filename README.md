# Vivino Market Analysis

A team project @ [BeCode.org](https://becode.org/) as part of the **AI Bootcamp** in Gent

## Project description

This is a project to create a visualization model to help Vivino do some analysis of their data around the world.

To carry out this visualization we will have as a base the following Vivino database, which has the following structure: 

![Vivino DB](/vivino_market_analysis/assets/vivino_db_diagram_horizontal.png)

The data used it come from a `db` file from Vivino company, provided as part of the initial exercise  [here](https://drive.google.com/file/d/122rj3-c0mpFPL04IXeXjSp2_H66-33RS/view?usp=sharing).

## Installation

1. Clone [wine_market_analysis](https://github.com/mendoce24/wine_market_analysis.git) repository
2. Change directory to the root of the repository
3. Install required libraries by running `pip install -r requirements.txt`

## Conclusions
As a result of our analysis, browsing the database provided, we were able to observe the following:

- To highlight 10 wines to increase the sales, we decided to used a list with the most affordable wines with a good score, which vintages are in the top list of the ranking.

- We have a marketing budget for this year. Which country should we To prioritise the marketing in one country, argentina is going to the best option becouse because even though it does not have a large number of registered users, its consumption of algohol has been increasing year after year, in addition, `Argentine` wines are some of the best ranked on the market. 
Currently only 1,37 % of Argentininans uses Vivino, so there's a lot of room to grow in this country of 46 million, a sizeable population.
And Argentininans like wine: they are only 7th when it comes to yearly wine consumption, but the wine consumption grew by 6,3 percent in 2019 alone and the Compound annual growth rate (CAGR) is 23,90 percent whereas CAGR is in decline in most countries.
So Argentininans like wine, wine consumption is growing but we do not have a lot Argentininan Vivino users yet.
![FocusOnArgentina](/output/FocusOnArgentina.png)
- If we take into account the wines with the keywords `(coffee, toast, green apple, cream, citrus)` We cant get only 16 wines which have this combination, but more peopel think that the `Brut Champagne` have been more identificated with those keywords.

- Taking (`Cabernet Sauvignon`, `Merlot`, `Chardonnay`) like the 3 most common grapes all over the world. We selected wines that were produced in these countries in which the top 3 grapes are grown.

- Taking the `average rating wines` for each country we can find that `Israel` is the country leaderboard with `4.5` rating, but with an other `average rating` taking from `vintages` we can find that `Romania` is the country leaderboard.
![FocusOnArgentina](/output/CountryLeaderboard.png)


### Deployment
- To have a clearer view of the data presented, it will be shown in `src/appy.py` application launched in `Streamlit` which shows the different questions presented by Vivino and the visualization and response presented by the working group:



## Timeline

One week project, in the week of August 27-31, 2023.

presentation in September 01, 2023.

## The Team

The project was made by:

- Team Lead (Data Engineer): César E. Mendoza V. [LinkedIn](https://www.linkedin.com/in/mendoce24/) | [GitHub](https://github.com/mendoce24)
- Data Analyst: Fré Van Oers [LinkedIn](https://www.linkedin.com/in/frevanoers/) | [GitHub](https://github.com/DeFre)
- Data Engineer:  Sam Valdeman [LinkedIn](https://www.linkedin.com/in/sam-veldeman-b0307b233/) | [GitHub](https://github.com/Sam-Veldeman)

## Instruction

The stage was made under the supervision of [Vanessa Rivera Quiñones](https://www.linkedin.com/in/vriveraq/) and [Samuel Borms](https://www.linkedin.com/in/sam-borms/?originalSubdomain=be)

Gent | Augustus 31, 2023
