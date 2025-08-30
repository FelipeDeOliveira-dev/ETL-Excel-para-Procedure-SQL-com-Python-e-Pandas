import pandas as pd


class Xlsx:
    def __init__(self, file):
        self.file = file
        self.df = pd.read_excel(file)

    def show_xlsx(self, n=100):
        print(self.df.head(n))

    def info_xlsx(self):
        print(self.df.info())