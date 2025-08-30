import pandas as pd

def xlsx(file):
    df = pd.read_excel(file)
    return print(df.head(100))
