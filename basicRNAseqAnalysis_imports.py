##static params
baseDir='/home/jovyan/efs/all_seq/rnaseq_merged/' #Base directory

import warnings
warnings.filterwarnings('ignore')
import ipywidgets as widgets
import os
import pandas as pd
from IPython.display import display,Javascript
from ipywidgets import  Layout


def run_all(ev):
    display(Javascript('IPython.notebook.execute_cells_below()'))

exampleQuery='B-Cell,T-Cell' 
style = {'description_width': 'initial'}
widget_query=widgets.Text(
    #value='',
    placeholder='Enter conditions seperated by comma to search and compare: eg. B-Cell,T-Cell',
    description='',
    disabled=False,
    #description='(50% width, 80px height) button',
    layout=widgets.Layout(width='50%', height='50px'),
    style=style
    
)

baseDir_FnameS=pd.Series(os.listdir(baseDir))
speciesWithReprocessedData=baseDir_FnameS[baseDir_FnameS.str.contains('.npy$')].str.split('.').str[0].unique()

widget_specie=widgets.Select(
    options=speciesWithReprocessedData,
    value='Homo_sapiens',
    # rows=10,
    description='Select your species:',
    disabled=False,
    style=style
)

button_query = widgets.Button(description="Search and compare",
                             layout=Layout(width='20%', height='10%'))
button_query.on_click(run_all)
button_query.style.button_color='lightblue'
accordion = widgets.HBox(children=[widget_query,button_query])