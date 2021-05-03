import csv
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    temperature = []
    ice_cream_sales = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            temperature.append(float(row["Temperature"]))
            ice_cream_sales.append(float(row["Ice-cream Sales"]))
    return {"x" : temperature, "y" : ice_cream_sales}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("Correlation between temperature vs ice cream sales: ", correlation[0, 1])

def setup():
    data_path = "C:/Users/sravy/White Hat Jr/C 106- Correlation/Ice cream vs cold drink vs temperature.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)

setup()