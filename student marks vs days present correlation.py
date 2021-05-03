import csv
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    student_marks = []
    days_present = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            student_marks.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))
    return {"x" : student_marks, "y" : days_present}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("Correlation between marks in percentage and days present: ", correlation[0, 1])

def setup():
    data_path = "C:/Users/sravy/White Hat Jr/C 106- Correlation/student marks vs days present.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)

setup()