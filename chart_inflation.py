import plotly.graph_objects as go
import pandas as pd
import statics
from base import conn



def chart_burn_DC(fig, interval_data, burned_dollars):
    '''
    '''

    fig.add_trace(go.Scatter(x=interval_data['Date'],
                        y=burned_dollars,
                        mode='lines',
                        name='Burned',
                        yaxis="y2",
                        # marker=dict(
                        #     size=5,
                        #     color='#ff5252',
                        #     symbol='circle',
                        #     line = {'width':1}, # line around marker
                        # ),
                        line=dict(
                            color='#ffcc00',
                            width=2,
                        )))


    fig.add_trace(go.Bar(
        name='State channel',
        x=interval_data['Date'],
        y=interval_data['State channel'],
        marker=dict(
            color = '#ce481c',
            line = {'width':0}, # line around marker
        ),
    ))


    fig.add_trace(go.Bar(
        name='Fee',
        x=interval_data['Date'],
        y=interval_data['Fee'],
        marker=dict(
            color = '#b30d73',
            line = {'width':0}, # line around marker
        ),
    ))


    fig.add_trace(go.Bar(
        name='Assert location',
        x=interval_data['Date'],
        y=interval_data['Assert location'],
        marker=dict(
            color = '#01a39e',
            line = {'width':0}, # line around marker
        ),
    ))


    fig.add_trace(go.Bar(
        name='Add gateway',
        legendgrouptitle=dict(font=dict(size=20)),
        x=interval_data['Date'],
        y=interval_data['Add gateway'],
        marker=dict(
            color = '#660066',
            line = {'width':0}, # line around marker
        ),
        #marker_color='#0a9ad7',
    ))


    fig.update_layout(
        legend=dict(title_font_family="Times New Roman",
                                font=dict(size= 20)),
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
            range=(0,burned_dollars.max() + burned_dollars.max()*10/100),
            title="Burned dollars($)",
            titlefont=dict(
                color="#ffcc00",
                size=25,
            ),
            tickfont=dict(
                color="#ffcc00",
                size=20,
            ),
            anchor="free",
            overlaying="y",
            side="left",
            position=0.05,
            linecolor="#ffcc00"
        ),
    )


    fig.update_layout(
        plot_bgcolor=statics.COLORS['background'],
        paper_bgcolor=statics.COLORS['background'],
        font_color=statics.COLORS['text'],
        font_family=statics.FONT,
    )


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


    burn_HNT = df_burnDC.drop(['id', 'timestamp', 'Interval', 'State channel', 'Fee', 'Assert location', 'Add gateway'], axis = 1).set_index('Date')
    #print(burn_HNT)
    price_close = df_PriceHNT.drop(['id', 'coin_id', 'timestamp', 'Interval', 'Open', 'High', 'Low', 'Volume'], axis = 1).set_index('Date')
    #print(price_close)
    df = pd.concat([burn_HNT,price_close], axis=0).ffill().bfill()
    print(df)

    df_burned_HNT = pd.DataFrame(data).set_index('Date', inplace=True)
    
    #print(df_burned_HNT)
    ##df_burned_HNT = pd.Series((df_burnDC['total']* statics.DC_PRICE) / df_PriceHNT['Close'])
    df_burned_HNT.set_index('Date', inplace=True)
    print(df_burned_HNT)
    print(df_burnDC.dtypes)

    

    df_burnDC_1d = df_burnDC[df_burnDC['Interval'].str.contains('1d')]
    burned_dolars = pd.Series(df_burnDC_1d['total'] * statics.DC_PRICE)

    chart_burn_DC(fig, df_burnDC_1d, burned_dolars)


