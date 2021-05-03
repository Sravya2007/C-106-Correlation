import pandas as pd
import plotly.express as px

df = pd.read_csv("C:/Users/sravy/White Hat Jr/C 106- Correlation/student marks vs days present.csv")
fig = px.scatter(df, x="Marks In Percentage", y="Days Present")
fig.show()