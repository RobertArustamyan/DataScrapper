import pandas as pd

def converter():
    df = pd.read_csv("../Data/result.csv", encoding='utf-8')
    df.to_excel('output.xlsx', index=False)