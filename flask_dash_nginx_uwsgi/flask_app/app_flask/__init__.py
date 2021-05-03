from flask import Flask
import dash
import dash_auth
import dash_bootstrap_components as dbc
import os

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])

VALID_USERNAME_PASSWORD_PAIRS = {
        os.getenv('USER_NAME'): os.getenv('USER_PASS')
    }

auth = dash_auth.BasicAuth(
        app,
        VALID_USERNAME_PASSWORD_PAIRS
    )

from app_flask import views