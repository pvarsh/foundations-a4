import os
import csv
import numpy as np
import pandas as pd

path = "../data/State_County"
#print os.listdir(path)

fname = path + '/' + '2002_carbon_per_county_resaved.csv'
with open(fname, 'rU') as f:
    #dfCarbon = pd.read_csv(f, header = 3)
    reader = csv.reader(f)
    for i, line in enumerate(reader):
        if i < 20:
            print line
#print df


