from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd

from app import *
from components import sidebar, extratos, dashboards

from globals import *

df_receitas = pd.read_csv("df_receitas.csv", index_col=0, parse_dates=True)
df_receitas_aux = df_receitas.to_dict()

df_despesas = pd.read_csv("df_despesas.csv", index_col=0, parse_dates=True)
df_despesas_aux = df_despesas.to_dict()

list_receitas = pd.read_csv('df_cat_receita.csv', index_col=0)
list_receitas_aux = list_receitas.to_dict()

list_despesas = pd.read_csv('df_cat_despesa.csv', index_col=0)
list_despesas_aux = list_despesas.to_dict()


# =========  Layout  =========== #
content = html.Div(id="page-content")


app.layout = dbc.Container(children=[
    dcc.Store(id="store-receitas", data=df_receitas.to_dict()),
    dcc.Store(id="store-despesas", data=df_despesas_aux),
    dcc.Store(id='stored-cat-receitas', data=list_receitas_aux),
    dcc.Store(id='stored-cat-despesas', data=list_despesas_aux),

    dbc.Row([
        dbc.Col([
            dcc.Location(id="url"),
            sidebar.layout
        ], md=2),

        dbc.Col([
            content
        ], md=10)
    ])

], fluid=True,)

@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page(pathname):
    if pathname == "/" or pathname == "/dashboards":
        return dashboards.layout
    
    if pathname == "/extratos":
        return extratos.layout


if __name__ == '__main__':
    app.run_server(port=8051, debug=True)