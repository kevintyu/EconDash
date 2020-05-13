# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app = dash.Dash(__name__)

df = pd.read_csv('CAN_Bond_Benchmark_Yield.csv')
data = [go.Scatter{

}

]
app.layout = html.Div ([

])
if __name__ == '__main__':
    app.run_server(debug=True)
