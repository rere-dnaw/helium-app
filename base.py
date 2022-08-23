from dash import Dash
import dash_bootstrap_components as dbc
import sqlite3


app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.DARKLY],    
    meta_tags=[
        {
            "name": "viewport",
            "content": "width=device-width, initial-scale=1.0, maximum-scale=1",
        }
    ],)

conn = sqlite3.connect('/home/l080lap/Documents/1.Programming/python/helium/helium-sql/dbHeliumApp.db') 
