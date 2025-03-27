from dash import html, dcc

navbar = html.Nav([
    dcc.Link("Analyse", href="/analyse", className="nav-link"),
    dcc.Link("Dashboard", href="/dashboard", className="nav-link"),
    dcc.Link("Backtest", href="/backtest", className="nav-link"),
    dcc.Link("Education", href="/education", className="nav-link"),
    dcc.Link("LAB", href="/lab", className="nav-link"),
], className="navbar navbar-expand-lg navbar-dark bg-dark px-3")
