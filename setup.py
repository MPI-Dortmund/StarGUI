from setuptools import setup, find_packages


setup(
    name='stargui',
    version="0.2.0",
    python_requires='3.10',
    packages=find_packages(),
    url='',
    license='MIT',
    author='Gavin Rice',
    install_requires=[
        "argparse = 1.4.0",
        "pandas = 1.4.3",
        "starfile = 0.4.11",
        "numpy = 1.23.0",
        "pandasgui = 0.2.13"
    ],
    author_email='gavin.rice@mpi-dortmund.mpg.de',
    description='Starfile manipulation scripts and interactive GUI',
    long_description='',
    long_description_content_type='text/markdown',
    entry_points={
        'console_scripts': [
            'stargui_viz = scripts.stargui_viz:_main_',
            'stargui_addconstant = scripts.stargui_addconstant:_main_',
            'stargui_addcsv = scripts.stargui_addcsv:_main_',
            'stargui_combine_stars = scripts.stargui_combine_stars:_main_',
            'stargui_randomize_values = scripts.stargui_randomize_values:_main_',
            'stargui_string_replacer = scripts.stargui_stringreplace:_main_',
            'stargui_sum_columns = scripts.stargui_sumcolumns:_main_',
        ]},
)
