# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output
# import plotly.graph_objects as go
# from plotly.subplots import make_subplots

# app = dash.Dash(__name__)

# app.layout = html.Div([
#     dcc.Graph(id="graph"),
#     html.P("Red line's axis:"),
#     dcc.RadioItems(
#         id='radio',
#         value='Secondary',
#         options=[{'label': x, 'value': x}
#                  for x in ['Primary', 'Secondary']]
#     )
# ])

# @app.callback(
#     Output("graph", "figure"), 
#     [Input("radio", "value")])
# def display_(radio_value):

#     # Create figure with secondary y-axis
#     fig = make_subplots(specs=[[{"secondary_y": True}]])

#     # Add traces
#     fig.add_trace(
#         go.Scatter(x=[1, 2, 3], y=[40, 50, 60], name="yaxis data"),
#         secondary_y=False,
#     )

#     fig.add_trace(
#         go.Scatter(x=[2, 3, 4], y=[4, 5, 6], name="yaxis2 data"),
#         secondary_y=radio_value == 'Secondary',
#     )

#     # Add figure title
#     fig.update_layout(
#         title_text="Double Y Axis Example"
#     )

#     # Set x-axis title
#     fig.update_xaxes(title_text="xaxis title")

#     # Set y-axes titles
#     fig.update_yaxes(
#         title_text="<b>primary</b> yaxis title", 
#         secondary_y=False)
#     fig.update_yaxes(
#         title_text="<b>secondary</b> yaxis title", 
#         secondary_y=True)

#     return fig

# app.run_server(debug=True)


from dash import Dash, dcc, html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash()

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
            dcc.Graph(
                id='graph-1-tabs',
                figure={
                    'data': [{
                        'x': [1, 2, 3],
                        'y': [3, 1, 2],
                        'type': 'bar'
                    }]
                }
            )
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




# fig.add_trace(go.Scatter(x=df_1h['Date'],
#                     y=df_1h['total'],
#                     mode='lines+markers',
#                     name='test-name',
#                     marker=dict(
#                         size=7,
#                         color='#ff5252',
#                         symbol='circle',
#                         line = {'width':1}, # line around marker
#                     ),
#                     line=dict(
#                         color='#ff7f0e',
#                         width=3,
#                     ),
#                     yaxis="y2"))




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