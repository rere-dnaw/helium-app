from dash import Dash
import sqlite3


app = Dash(    
    meta_tags=[
        {
            "name": "viewport",
            "content": "width=device-width, initial-scale=1, maximum-scale=1",
        }
    ],)

conn = sqlite3.connect('/mnt/Data/1.Programming/helium/helium-sql/dbHeliumApp.db') 
