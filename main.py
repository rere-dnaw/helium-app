from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import chart_burn_DC
import chart_inflation
from base import app


fig_burnDC = go.Figure()
chart_burn_DC.create_chart_burn_DC(fig_burnDC)


fig_inflation = go.Figure()
chart_inflation.create_chart_inflation(fig_inflation)


app.layout = html.Div([
    html.H1('Helium data', className='title_style'),
    dcc.Tabs(
        id="tabs_component",
        value='tab_burn_DC',
        parent_className='custom-tabs',
        className='custom-tabs-container',
        children=[
            dcc.Tab(
                label='Burned DC',
                value='tab_burn_DC',
                className='custom-tab',
                selected_className='custom-tab--selected',
            ),
            dcc.Tab(
                label='Inflation-Burn',
                value='tab_burn_infla',
                className='custom-tab',
                selected_className='custom-tab--selected',
            ),
        ]),
    html.Div(id='tabs-content-example-graph', className='div_test')
], className='div_test')

@app.callback(Output('tabs-content-example-graph', 'children'),
              Input('tabs_component', 'value'))
def render_content(tab):
    if tab == 'tab_burn_DC':
        return html.Div([
            dcc.Graph(id='example,',
            figure=fig_burnDC,
            style={'height': '80vh'})
        ])
    elif tab == 'tab_burn_infla':
        return html.Div([
            dcc.Graph(
                id='graph-2-tabs',
                figure=fig_inflation,
                style={'height': '80vh'})
        ])

if __name__ == '__main__':
    app.run_server()
