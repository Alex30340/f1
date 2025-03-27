from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
from core.app_instance import app
from components.navbar import navbar
import pages.analyse, pages.dashboard, pages.backtest, pages.education, pages.lab

app.layout = html.Div([
    dcc.Location(id='url'),
    navbar,
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'), Input('url', 'pathname'))
def display_page(pathname):
    if pathname == "/analyse":
        return pages.analyse.layout
    elif pathname == "/dashboard":
        return pages.dashboard.layout
    elif pathname == "/backtest":
        return pages.backtest.layout
    elif pathname == "/education":
        return pages.education.layout
    elif pathname == "/lab":
        return pages.lab.layout
    else:
        return html.H1("Page non trouvée", style={"padding": "100px", "color": "red"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
