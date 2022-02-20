from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import sqlite3
import pandas as pd
import statics
import chart_burn_DC



app = Dash()

conn = sqlite3.connect('/mnt/Data/1.Programming/helium/helium-sql/dbHeliumApp.db') 

sql_query = pd.read_sql_query ('''
                               SELECT
                               *
                               FROM BurnedDC
                               ''', conn)

df = pd.DataFrame(sql_query)

df_1d = df[df['Interval'].str.contains('1d')]
burned_dolars = pd.Series(df_1d['total'] * statics.DC_PRICE)

burnDCchart = go.Figure()
chart_burn_DC.burn_DC_chart(burnDCchart, df_1d, burned_dolars)

app.layout = html.Div([
    html.H1('Dash Tabs component demo'),
    dcc.Tabs(id="tabs-example-graph", value='tab-1-example-graph', children=[
        dcc.Tab(label='Tab One', value='tab-1-example-graph'),
        dcc.Tab(label='Tab Two', value='tab-2-example-graph'),
    ]),
    html.Div(id='tabs-content-example-graph')
])

@app.callback(Output('tabs-content-example-graph', 'children'),
              Input('tabs-example-graph', 'value'))
def render_content(tab):
    if tab == 'tab-1-example-graph':
        return html.Div([
            html.H3('Tab content 1'),
            dcc.Graph(id='example,',
            figure=burnDCchart)
        ])
    elif tab == 'tab-2-example-graph':
        return html.Div([
            html.H3('Tab content 2'),
            dcc.Graph(
                id='graph-2-tabs',
                figure={
                    'data': [{
                        'x': [1, 2, 3],
                        'y': [5, 10, 6],
                        'type': 'bar'
                    }]
                }
            )
        ])

if __name__ == '__main__':
    app.run_server(debug=True)
