import pandas as pd
import plotly.express as px

df = pd.read_csv("C:/Users/sravy/White Hat Jr/C 106- Correlation/Ice cream vs cold drink vs temperature.csv")
fig = px.scatter(df, x="Temperature", y="Ice-cream Sales( ₹ )")
fig.show()