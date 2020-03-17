import pandas as pd
import converter
from converter import uni512zg1,zg12uni51,test
import re


df = pd.read_csv("./data/sample_data.csv", usecols = ['Full Story'])
print(df)
# regExp = "[(+*$@!?/\,+-_=|''"";:။၊၁၂၃၄၅၆၇၈၉၀)a-zA-Z\s]"
regExp = "[(+{}()*$@![]?/\,+-_=–|''"";:&^%#။၊၁၂၃၄၅၆၇၈၉၀“”‘)a-zA-Z\s]"
for index,row in df.iterrows():
    text = row['Full Story']
    input = zg12uni51(text)
    output = re.sub(regExp,'',input)
    print(output)


