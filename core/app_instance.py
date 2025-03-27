from dash import Dash
import dash_bootstrap_components as dbc

app = Dash(
    __name__,
    use_pages=True,  # ← Important pour que les pages fonctionnent
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True  # ← Utile pour les callbacks définis dans les pages
)

server = app.server