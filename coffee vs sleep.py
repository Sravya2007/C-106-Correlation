import pandas as pd
import plotly.express as px

df = pd.read_csv("C:/Users/sravy/White Hat Jr/C 106- Correlation/cups of coffee vs hours of sleep.csv")
fig = px.scatter(df, x="Coffee in ml", y="sleep in hours")
fig.show()