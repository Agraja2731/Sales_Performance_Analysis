# Python Script for Data Analysis
import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

# Perform basic analysis
print(df.describe())
