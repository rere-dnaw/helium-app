from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import chart_burn_DC
import chart_inflation
import chart_price
from base import app


fig_burnDC = go.Figure()
chart_burn_DC.create_chart_burn_DC(fig_burnDC)


fig_inflation = go.Figure()
chart_inflation.create_chart_inflation(fig_inflation)

fig_price = go.Figure()
chart_price.create_chart_price(fig_price)


app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("HELIUM DATA",
                        className='text-center text-white align-text-bottom m-5 font-weight-bold'),
                width=12)
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Tabs(
                [
                    dbc.Tab(label='Burned DC',tab_id='tab_burn_DC'),
                    dbc.Tab(label='Inflation-Burn',tab_id='tab_burn_infla'),
                    dbc.Tab(label='Chart price',tab_id='chart_price'),
                ],
                id="tabs",
                active_tab='tab_burn_DC',
            ),
            html.Div(id='tabs-content')
        ],
        width={'size':12},
        )
    ], justify='center')
], fluid=True)


@app.callback(Output('tabs-content', 'children'),
              Input('tabs', 'active_tab'))
def render_content(tab):
    if tab == 'tab_burn_DC':
        return html.Div([
            dcc.Graph(id='graph-1-tab',
            figure=fig_burnDC,
            style={'height': '80vh'})
        ])
    elif tab == 'tab_burn_infla':
        return html.Div([
            dcc.Graph(
                id='graph-2-tab',
                figure=fig_inflation,
                style={'height': '80vh'})
        ])
    elif tab == 'chart_price':
        return html.Div([
            dcc.Graph(
                id='graph-3-tab',
                figure=fig_price,
                style={'height': '80vh'})
        ])

if __name__ == '__main__':
    app.run_server()