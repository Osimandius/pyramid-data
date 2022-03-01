import plotly.express as px
import plotly.figure_factory as ff
import csv
import pandas as pd

df=pd.read_csv("HeightWeight.csv")

fig = ff.create_distplot([df["Weight(Pounds)"].tolist()],["Fatness"], show_hist=False)
fig.show()