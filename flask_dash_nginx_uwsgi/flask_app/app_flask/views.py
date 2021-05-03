from app_flask import app
import os
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

app.layout = dbc.Container([
        dbc.Row([
            dbc.Col(
                html.H1('Dashboard', className='text-center tex-primary, display-2 shadow-lg'),
                width=10)
            ]

        )
    ], fluid=True)