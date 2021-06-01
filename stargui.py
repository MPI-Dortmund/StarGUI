# Author: Gavin Rice
# Date 19.04.21
# Opens a starfile in pandasgui for easy visualization and manipulation.
# Also prints your starfile as a DataFrame before opening.
# PandasGUI: pypi.org/project/pandasgui/
# Starfile: github.com/alisterburt/starfile

import os
import argparse
import starfile
import pandas as pd
from pandasgui import show

parser = argparse.ArgumentParser(description='Open star file with graphical user interface')
parser.add_argument('--star', dest="filename", required=True,
                   help='Path to star file to open', metavar="FILE")
args = parser.parse_args()

STAR = args.filename

df = starfile.open(STAR)
print(df)
show(df)

