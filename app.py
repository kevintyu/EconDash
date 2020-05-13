# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# hello
# Kelvin Du & Gordon Tang
import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.express as px
import plotly.graph_objs as go

import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

# app = dash.Dash()
# df = pd.read_csv('CAN_Bond_Benchmark_Yield.csv')
#
# fig = px.line(df, x='Date', y='')

if __name__ == '__main__':
    app.run_server(debug=True)




# app = dash.Dash(__name__)
#
# df = pd.read_csv('CAN_Bond_Benchmark_Yield.csv')
# data = [go.Scatter{
#             x=df.Date,
#             y=df[]
#
# }
#
# ]
# app.layout = html.Div ([
#
# ])
if __name__ == '__main__':
    app.run_server(debug=True)
