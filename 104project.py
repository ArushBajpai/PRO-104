import pandas as pd
import statistics as st

data = pd.read_csv("SOCR-HeightWeight.csv")

height = data["Height(Inches)"].tolist()

weight = data["Weight(Pounds)"].tolist()

height_mean = st.mean(height)
weight_mean = st.mean(weight)

print(height_mean,weight_mean)

height_median = st.median(height)
weight_median = st.median(weight)

print(height_median,weight_median)

height_mode = st.mode(height)
weight_mode = st.mode(weight)

print(height_mode,weight_mode)
