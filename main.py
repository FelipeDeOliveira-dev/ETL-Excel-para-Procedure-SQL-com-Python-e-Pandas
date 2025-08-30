import pandas as pd
import numpy as np
import openpyxl
import os
from models import *

file = r"C:\Users\junio\OneDrive\Área de Trabalho\SQLAutomative\modelo.xlsx"
xlsx = Xlsx(file)


xlsx.xlsx()
xlsx.info_xlsx()