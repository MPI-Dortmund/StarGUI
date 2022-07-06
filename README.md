# StarGUI
Making star file manipulation easy with Pandas and a GUI

## Local Installation
conda create -y -n stargui python==3.10
python setup.py sdist
pip install dist/


## Requirements
Python 3.10

argparse 1.4.0

pandas 1.4.3

numpy 1.23.0

pandasgui 0.2.13

starfile 0.4.11

## Current tools
* stargui_viz: main GUI with interactive versions of all commands (in development)
* addconstant: adds a new column with a constant value
* addcsv: adds a new column to a star file with values from a CSV list
* combine_stars: adds a column from one star file to another
* randomize_values: randomizes the values in a column
* stringreplace: replace or remove any text string using a stringsearch
* sumcolumns: adds two column values together and replaces the first column values with the sum

## To Do
* Make things work with multi-datatable star files
* GUI in progress