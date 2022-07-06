import os
import argparse
import starfile
import pandas as pd
import numpy as np

parser = argparse.ArgumentParser(description='Randomizes the values of a column between -180 and 180')
parser.add_argument('--star', dest="filename", required=True,
                   help='Path to star file to open', metavar="FILE")
parser.add_argument('--label', type=str, required=True,
                   help='Name of the column randomize values in')
args = parser.parse_args()

STAR = args.filename
NAME = args.label

df = starfile.read(STAR)
print(df)
print(df[NAME])
df[NAME] = (np.random.randint(-180, 180, size=len(df)))
print(df)
starfile.write(df, 'new.star')
print("Wrote new.star in current directory.")