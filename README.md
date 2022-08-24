# helium-app
Displays charts for data created through `helium-sql`. The app is using dash, plotly for creating charts.

The app require `statics.py` file for working which is not included in the repository.

 `statics.py` 
```python 
COLORS = {'background':'#0D1F2D',

'text':'#ffffff'}

FONT = "Courier New"

DC_PRICE = 0.00001 # the price of data credits in helium network

DB_LOCATION = ".../helium-sql/dbHeliumApp.db"
```

The database can be created through app from another repository:
https://github.com/rere-dnaw/helium-sql
