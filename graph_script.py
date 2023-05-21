import pandas as pd
import numpy as np
import matplotlib

df = pd.read_csv("PrecipitationData.csv")
df.set_index(df["Time"], inplace = True)
df = df.iloc[:, 2:]
print(df)
df.to_csv("PrecipitationData.csv")
