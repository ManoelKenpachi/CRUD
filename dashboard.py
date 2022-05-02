from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import pathlib

client = Dash(__name__)

df = pd.read_csv(f'{pathlib.Path(__file__).parent.absolute()}\\data.csv', encoding='UTF8')
df = df.fillna('')

fig = px.bar(df, x="e", y="qtd_p", color="s", barmode="group")

client.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Quantidade de produtos venditos por ticket de cada Estado e seu status de venda.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    client.run_server(debug=True)