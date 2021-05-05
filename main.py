import pandas as pd
import numpy as np
import xlrd
import openpyxl

# Zad1
dtFrame = pd.read_excel('imiona.xlsx', header=0)
# print(dtFrame)
# Zad2
# print(dtFrame.loc[dtFrame['Liczba'] < 1000])
# print(dtFrame.loc[dtFrame['Imie']=='BOHDAN'])
# print(dtFrame['Liczba'].sum())
# Pomocniczy dataframe
dt1=dtFrame.loc[(dtFrame['Rok']>2005) & (dtFrame['Rok']<2010)]
# print(dt1['Liczba'].sum())