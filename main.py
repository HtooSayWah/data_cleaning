import pandas as pd
import converter
from converter import uni512zg1,zg12uni51,test


df = pd.read_csv("./data/sample_data.csv", usecols = ['Full Story'])
print(df)
text = df[1:2]
print(zg12uni51(text.to_string()))


