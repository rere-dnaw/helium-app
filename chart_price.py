import plotly.graph_objects as go
import pandas as pd
import statics
from base import conn



def chart_price(fig, df_fear_greed, df_PriceHNT, df_PriceBTC):
    '''
    fig, df_burned, df_rewards, df_supply
    '''

    fig.add_trace(go.Scatter(x=df_PriceBTC['Date'],
                        y=df_PriceBTC['Close'],
                        mode='lines',
                        name='Index value',
                        line=dict(
                            color='#ce481c',
                            width=3,
                        )))

    fig.add_trace(go.Scatter(x=df_PriceHNT['Date'],
                        y=df_PriceHNT['Close'],
                        mode='lines',
                        name='HNT price',
                        yaxis="y2",
                        line=dict(
                            color='#01a39e',
                            width=3,
                        )))
    
    fig.add_trace(go.Scatter(x=df_fear_greed['Date'],
                        y=df_fear_greed['Value'],
                        mode='lines',
                        name='BTC price',
                        yaxis="y3",
                        line=dict(
                            color='#ffcc00',
                            width=3,
                        )))

    fig.update_layout(
        legend=dict(title_font_family="Times New Roman",
                    font=dict(size= 20),
                    orientation="h",
                    x=0.5),
        xaxis=dict(
            domain=[0.10, 1],
            gridcolor="white",
            title="Time frame",
            titlefont=dict(
                color="white",
                size=25,
            ),
            tickfont=dict(
                color="white",
                size=20,
            ),
            
        ),
        yaxis=dict(
            gridcolor="#ce481c",
            #title="BTC Price",
            titlefont=dict(
                color="#ce481c",
                size=25,
            ),
            tickfont=dict(
                color="#ce481c",
                size=20,
            ),
            side="right",
            
        ),
        yaxis2=dict(
            gridcolor="#01a39e",
            #range=(0,df_fear_greed['Value'].max() + df_fear_greed['Value'].max()*10/100),
            #title="Index Value",
            titlefont=dict(
                color="#01a39e",
                size=25,
            ),
            tickfont=dict(
                color="#01a39e",
                size=20,
            ),
            anchor="x",
            overlaying="y",
            side="right",
            linecolor="white"
        ),
        yaxis3=dict(
            gridcolor="#ffcc00",
            #range=(0,df_fear_greed['Value'].max() + df_fear_greed['Value'].max()*10/100),
            #title="HNT circulating supply",
            titlefont=dict(
                color="#ffcc00",
                size=25,
            ),
            tickfont=dict(
                color="#ffcc00",
                size=20,
            ),
            anchor="x",
            overlaying="y",
            
            linecolor="white"
        ),
    )


    fig.update_layout(
        margin=dict(
            l=0,  # left margin
            r=20,  # right margin
            b=10,  # bottom margin
            t=10),
        plot_bgcolor=statics.COLORS['background'],
        paper_bgcolor=statics.COLORS['background'],
        font_color=statics.COLORS['text'],
        font_family=statics.FONT,
    )

    fig.update_yaxes(automargin=True)

def create_chart_price(fig):
    '''
    '''
    sql_query = pd.read_sql_query ('''
                               SELECT
                               *
                               FROM 'FearGreed'
                               ''', conn)
    df_fear_greed = pd.DataFrame(sql_query)

    #### get ID hor HNT coin
    sql_query = pd.read_sql_query ('''
                                SELECT
                                ID
                                FROM Coins
                                WHERE
                                Name LIKE 'HNT/USDT'
                                ''', conn)
    idHNT = int(pd.DataFrame(sql_query)['id'][0])

    #### get ID hor BTC coin
    sql_query = pd.read_sql_query ('''
                                SELECT
                                ID
                                FROM Coins
                                WHERE
                                Name LIKE 'BTC/USDT'
                                ''', conn)
    idBTC = int(pd.DataFrame(sql_query)['id'][0])

    sql_query = pd.read_sql_query ('''
                                SELECT
                                *
                                FROM Prices
                                WHERE
                                coin_id = {0} AND
                                Interval LIKE '1d'
                                '''.format(idHNT), conn)
    df_PriceHNT = pd.DataFrame(sql_query)
    df_PriceHNT['Date'] = pd.to_datetime(df_PriceHNT['Date'])

    sql_query = pd.read_sql_query ('''
                                SELECT
                                *
                                FROM Prices
                                WHERE
                                coin_id = {0} AND
                                Interval LIKE '1d'
                                '''.format(idBTC), conn)
    df_PriceBTC = pd.DataFrame(sql_query)
    df_PriceBTC['Date'] = pd.to_datetime(df_PriceBTC['Date'])


    chart_price(fig, df_fear_greed, df_PriceHNT, df_PriceBTC)


