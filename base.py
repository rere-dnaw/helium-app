from dash import Dash
import sqlite3


app = Dash()

conn = sqlite3.connect('/mnt/Data/1.Programming/helium/helium-sql/dbHeliumApp.db') 
