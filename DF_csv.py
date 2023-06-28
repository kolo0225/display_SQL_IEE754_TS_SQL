# DF_csv.py

# Purpose:
#       exports pd.df in to CSV

# Packages:

import numpy as np
import pandas as pd
# ------------------------------------------------------------

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

class DFtoCSV:

    def __init__(self, df, path_csv): 

        # ------ instance variables ---------
        
        self.df            = df
        self.path_csv      = path_csv
        
	# --------------------- Top Bottom design -------------------
    
    # exports the df in to csv file
    def exports_file_csv(self):
        
        self.df.to_csv(self.path_csv)
