import dash 
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from datetime import date
import statics
from os.path import exists
import sqlite3




app = dash.Dash()

conn = sqlite3.connect('/mnt/Data/1.Programming/helium/helium-sql/dbHeliumApp2.db') 

sql_query = pd.read_sql_query ('''
                               SELECT
                               *
                               FROM BurnedDC
                               ''', conn)



df = pd.DataFrame(sql_query)

# sql_hnt_query = pd.read_sql_query ('''
#                                SELECT
#                                *
#                                FROM Coins
#                                ''', conn)


df_1d = df[df['Interval'].str.contains('1d')]
df_1h = df[df['Interval'].str.contains('1h')]

burned_dolars = pd.Series(df_1d['total'] * statics.DC_PRICE)


fig = go.Figure()

fig.add_trace(go.Scatter(x=df_1d['Date'],
                    y=burned_dolars,
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
    x=df_1d['Date'],
    y=df_1d['State channel'],
    marker=dict(
        color = '#ce481c',
        line = {'width':0}, # line around marker
    ),
))

fig.add_trace(go.Bar(
    name='Fee',
    x=df_1d['Date'],
    y=df_1d['Fee'],
    marker=dict(
        color = '#b30d73',
        line = {'width':0}, # line around marker
    ),
))

fig.add_trace(go.Bar(
    name='Assert location',
    x=df_1d['Date'],
    y=df_1d['Assert location'],
    marker=dict(
        color = '#01a39e',
        line = {'width':0}, # line around marker
    ),
))

fig.add_trace(go.Bar(
    name='Add gateway',
    legendgrouptitle=dict(font=dict(size=20)),
    x=df_1d['Date'],
    y=df_1d['Add gateway'],
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
        range=(0,burned_dolars.max() + burned_dolars.max()*10/100),
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


app.layout = html.Div(style={'backgroundColor': statics.COLORS['background']},children=[
    html.H1(
        children='Helium overview',
        style={
            'textAlign': 'center',
            'color': statics.COLORS['text'],
        }
    ),

    dcc.Graph(id='example,',
            figure=fig)
]
)




fig.show()










# data = [trace00]

# layout = go.Layout(title='Network forecast',
#                     xaxis = {'title': 'Timeframe'},
#                     yaxis = {'title': 'Amount burned'})


# fig = go.Figure(data=data,layout=layout)







if __name__ == '__main__':

    app.run_server()