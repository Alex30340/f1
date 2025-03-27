import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import pages.analyse
import pages.dashboard
import pages.backtest
import pages.education
import pages.lab

app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True  # ← Gère les callbacks de pages dynamiques
)

app.layout = html.Div([
    dcc.Location(id='url'),
    dbc.NavbarSimple(
        brand="Forex Analyzer",
        color="dark",
        dark=True,
        children=[
            dbc.NavItem(dcc.Link("Accueil", href="/", className="nav-link")),
            dbc.NavItem(dcc.Link("Analyse", href="/analyse", className="nav-link")),
            dbc.NavItem(dcc.Link("Dashboard", href="/dashboard", className="nav-link")),
            dbc.NavItem(dcc.Link("Backtest", href="/backtest", className="nav-link")),
            dbc.NavItem(dcc.Link("Éducation", href="/education", className="nav-link")),
            dbc.NavItem(dcc.Link("LAB", href="/lab", className="nav-link"))
        ]
    ),
    dash.page_container
])

if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0", port=8080)