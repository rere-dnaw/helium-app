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

conn = sqlite3.connect('/mnt/Data/1.Programming/helium/helium-sql/dbHeliumApp.db') 

sql_query = pd.read_sql_query ('''
                               SELECT
                               *
                               FROM BurnedDC
                               ''', conn)



df = pd.DataFrame(sql_query)

df_1d = df[df['Interval'].str.contains('1d')]
df_1h = df[df['Interval'].str.contains('1h')]

print(df)

fig = go.Figure()


fig.add_trace(go.Scatter(x=df_1d['Date'],
                    y=df_1d['total'],
                    mode='lines+markers',
                    name='test-name',
                    marker=dict(
                        size=7,
                        color='#ff5252',
                        symbol='circle',
                        line = {'width':1}, # line around marker
                    ),
                    line=dict(
                        color='#ff7b7b',
                        width=3,
                    )))


fig.add_trace(go.Scatter(x=df_1h['Date'],
                    y=df_1h['total'],
                    mode='lines+markers',
                    name='test-name',
                    marker=dict(
                        size=7,
                        color='#ff5252',
                        symbol='circle',
                        line = {'width':1}, # line around marker
                    ),
                    line=dict(
                        color='#ff7f0e',
                        width=3,
                    ),
                    yaxis="y2"))




# trace00 = go.Scatter(x=df_1d['Date'],
#                     y=df_1d['total'],
#                     mode='lines+markers',
#                     name='test-name',
#                     marker=dict(
#                         size=7,
#                         color='#ff5252',
#                         symbol='circle',
#                         line = {'width':1}, # line around marker
#                     ),
#                     line=dict(
#                         color='#ff7b7b',
#                         width=3,
#                     ))

# trace01 = go.Scatter(x=df_1d['Date'],
#                     y=df_1d['total'],
#                     mode='lines+markers',
#                     name='test-name',
#                     marker=dict(
#                         size=7,
#                         color='#ff5252',
#                         symbol='circle',
#                         line = {'width':1}, # line around marker
#                     ),
#                     line=dict(
#                         color='#ff7b7b',
#                         width=3,
#                     ))



fig.update_layout(
    xaxis=dict(
        domain=[0.3, 0.7]
    ),
    yaxis=dict(
        title="yaxis title",
        titlefont=dict(
            color="#1f77b4"
        ),
        tickfont=dict(
            color="#1f77b4"
        )
    ),
    yaxis2=dict(
        title="yaxis2 title",
        titlefont=dict(
            color="#ff7f0e"
        ),
        tickfont=dict(
            color="#ff7f0e"
        ),
        anchor="free",
        overlaying="y",
        side="left",
        position=0.15
    )
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