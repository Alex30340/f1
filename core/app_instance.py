from dash import Dash
import dash_bootstrap_components as dbc

app = Dash(__name__, use_pages=False, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
