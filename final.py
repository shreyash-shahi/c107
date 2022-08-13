import pandas as pd
import csv
import plotly.graph_objects as pg

df = pd.read_csv("datacsv.csv")
studentDf= df.loc[df['student_id']=="TRL_987"]
print(studentDf.groupby("level")['attempt'].mean())

fig = pg.Figure(pg.Bar(x=studentDf.groupby("level")['attempt'].mean(),
                       y=['Level1','Level2','Level3','Level4'],
                       orientation='h'))
fig.show()
