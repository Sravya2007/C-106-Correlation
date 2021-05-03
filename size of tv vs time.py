import pandas as pd
import plotly.express as px

df = pd.read_csv("C:/Users/sravy/White Hat Jr/C 106- Correlation/size of tv vs avg time spent watching tv.csv")
fig = px.scatter(df, x="Size of TV", y="	Average time spent watching TV in a week in hours")
fig.show()