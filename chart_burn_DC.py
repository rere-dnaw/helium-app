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
            anchor="x", #chnged from free
            overlaying="y",
            side="right",
            #position=0.05, #doesn't work when anchor in not free
            linecolor="#ffcc00"
        ),
    )


    fig.update_layout(
        plot_bgcolor=statics.COLORS['background'],
        paper_bgcolor=statics.COLORS['background'],
        font_color=statics.COLORS['text'],
        font_family=statics.FONT,
    )


def create_chart_burn_DC(fig):
    '''
    '''
    ### query for data from db
    sql_query = pd.read_sql_query ('''
                                SELECT
                                *
                                FROM BurnedDC
                                ''', conn)

    df_burnDC = pd.DataFrame(sql_query)

    df_burnDC_1d = df_burnDC[df_burnDC['Interval'].str.contains('1d')]
    burned_dolars = pd.Series(df_burnDC_1d['total'] * statics.DC_PRICE)

    chart_burn_DC(fig, df_burnDC_1d, burned_dolars)


