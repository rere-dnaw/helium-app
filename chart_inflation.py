import plotly.graph_objects as go
import pandas as pd
import statics
from base import conn



def chart_inflation_DC(fig, df_burned, df_rewards, df_supply):
    '''
    '''

    fig.add_trace(go.Scatter(x=df_supply['Date'],
                        y=df_supply['Supply amount'],
                        mode='lines',
                        name='Total supply',
                        yaxis="y2",
                        # marker=dict(
                        #     size=5,
                        #     color='#ff5252',
                        #     symbol='circle',
                        #     line = {'width':1}, # line around marker
                        # ),
                        line=dict(
                            color='#ce481c',
                            width=4,
                        )))


    fig.add_trace(go.Bar(
        name='Burned',
        x=df_burned['Date'],
        y=df_burned['Burned HNT'],
        marker=dict(
            color = '#660066',
            line = {'width':0}, # line around marker
        ),
    ))


    fig.add_trace(go.Bar(
        name='Rewards',
        x=df_rewards['Date'],
        y=df_rewards['Rewards'],
        marker=dict(
            color = '#01a39e',
            line = {'width':0}, # line around marker
        ),
    ))


    fig.update_layout(
        legend=dict(title_font_family="Times New Roman",
                                font=dict(size= 20),
                                orientation="h"),
        barmode='stack',
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
            title="DC Burn Totals",
            titlefont=dict(
                color="white",
                size=25,
            ),
            tickfont=dict(
                color="white",
                size=20,
            ),
            
        ),
        yaxis2=dict(
            gridcolor="#fcdc4d",
            automargin=True,
            range=(0,df_supply['Supply amount'].max() + df_supply['Supply amount'].max()*10/100),
            title="HNT circulating supply",
            titlefont=dict(
                color="#ce481c",
                size=25,
            ),
            tickfont=dict(
                color="#ce481c",
                size=20,
            ),
            anchor="x",
            overlaying="y",
            side="right",
            linecolor="white"
        ),
    )


    fig.update_layout(
        plot_bgcolor=statics.COLORS['background'],
        paper_bgcolor=statics.COLORS['background'],
        font_color=statics.COLORS['text'],
        font_family=statics.FONT,
    )

    fig.update_yaxes(automargin=True)

def create_chart_inflation(fig):
    '''
    '''
    ### query for data from db
    sql_query = pd.read_sql_query ('''
                                SELECT
                                *
                                FROM BurnedDC
                                WHERE
                                Interval LIKE '1d'
                                ''', conn)
    df_burnDC = pd.DataFrame(sql_query)

    sql_query = pd.read_sql_query ('''
                               SELECT
                               *
                               FROM 'Token Supply'
                               ''', conn)
    df_token_supply = pd.DataFrame(sql_query)

    sql_query = pd.read_sql_query ('''
                                SELECT
                                *
                                FROM RewardsHNT
                                ''', conn)
    df_rewardsHNT = pd.DataFrame(sql_query)

    #### get ID hor HNT coin
    sql_query = pd.read_sql_query ('''
                                SELECT
                                ID
                                FROM Coins
                                WHERE
                                Name LIKE 'HNT/USDT'
                                ''', conn)
    idHNT = int(pd.DataFrame(sql_query)['id'][0])

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


    df_burnDC['Date'] = pd.to_datetime(df_burnDC['Date'])
    ## this will add one day to each date column
    df_burnDC['Date']=df_burnDC.Date + pd.Timedelta(days=1)


    price_HNT = df_burnDC.drop(['id', 'timestamp', 'Interval', 'State channel', 'Fee', 'Assert location', 'Add gateway'], axis = 1)
    #print(burn_HNT)
    price_close = df_PriceHNT.drop(['id', 'coin_id', 'timestamp', 'Interval', 'Open', 'High', 'Low', 'Volume'], axis = 1)
    #print(price_close)
    burned_HNT = pd.merge(price_HNT, price_close, on = "Date", how = "inner")
    burned_HNT['Burned HNT'] = (burned_HNT['total'] * statics.DC_PRICE) / burned_HNT['Close']


    df_rewardsHNT = df_rewardsHNT.sort_values(by="Date")

    # print(burned_HNT)

    # print('t')


    chart_inflation_DC(fig, burned_HNT, df_rewardsHNT, df_token_supply)


