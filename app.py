import os
import io
import csv
import base64
import pandas as pd
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# Definir o backend do Matplotlib
os.environ['MPLBACKEND'] = 'TkAgg'

def read_csv_data(csv_file_path):
    df = pd.read_csv(csv_file_path, delimiter=';')
    return df

def create_horizontal_bar_chart_top(df):
    df_sorted = df.sort_values(by='casosAcumulado', ascending=False)
    top_cities = df_sorted.head(10)

    fig = go.Figure()

    fig.add_trace(go.Bar(
        y=top_cities['_id'],
        x=top_cities['casosAcumulado'],
        text=top_cities['casosAcumulado'],
        textposition='auto',
        name='Maiores Índices',
        orientation='h',
        marker=dict(color='blue')
    ))

    fig.update_layout(
        title='Top 10 Municípios com Maiores Índices de Casos Confirmados',
        xaxis_title='Casos Confirmados',
        yaxis_title='Cidade',
        barmode='stack'
    )

    return fig

def create_horizontal_bar_chart_bottom(df):
    df_sorted = df.sort_values(by='casosAcumulado', ascending=False)
    bottom_cities = df_sorted.tail(10)

    fig = go.Figure()

    fig.add_trace(go.Bar(
        y=bottom_cities['_id'],
        x=bottom_cities['casosAcumulado'],
        text=bottom_cities['casosAcumulado'],
        textposition='auto',
        name='Menores Índices',
        orientation='h',
        marker=dict(color='red')
    ))

    fig.update_layout(
        title='Top 10 Municípios com Menores Índices de Casos Confirmados',
        xaxis_title='Casos Confirmados',
        yaxis_title='Cidade',
        barmode='stack'
    )

    return fig

app.layout = html.Div([
    html.H1('Dashboard COVID-19'),

    dcc.Graph(id='horizontal-bar-chart-top'),
    dcc.Graph(id='horizontal-bar-chart-bottom'),
    dcc.Interval(
        id='interval-component',
        interval=60*1000,  # Atualiza os gráficos a cada 60 segundos
        n_intervals=0
    )
])

@app.callback(Output('horizontal-bar-chart-top', 'figure'), [Input('interval-component', 'n_intervals')])
def update_horizontal_bar_chart_top(n):
    csv_file_path = '/Users/batistajunior/Downloads/Projeto_covid_dados/covid_dados.csv'
    df = read_csv_data(csv_file_path)
    return create_horizontal_bar_chart_top(df)

@app.callback(Output('horizontal-bar-chart-bottom', 'figure'), [Input('interval-component', 'n_intervals')])
def update_horizontal_bar_chart_bottom(n):
    csv_file_path = '/Users/batistajunior/Downloads/Projeto_covid_dados/covid_dados.csv'
    df = read_csv_data(csv_file_path)
    return create_horizontal_bar_chart_bottom(df)

if __name__ == '__main__':
    app.run_server(debug=True)
