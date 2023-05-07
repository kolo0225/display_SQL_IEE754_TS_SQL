# DF_csv.py

# Purpose:
#       exports pd.df in to CSV

# Packages:
"""
import numpy as np
"""
import pandas as pd
"""
# files.py
from ImportSQliteDF import ImportsqlitelDF
"""
# path
#r"C:\ProgramData\CODESYS\CODESYSControlWinV3x64\94BCBDE7\PlcLogic\***.csv"         

# ####################################### universal variables #############################
#

# ------------- TEMP - ImportSQliteDF.py - VAR.---------- 
"""
# ----------------- variables:
# ImportSQliteDF:
# ---------------
db_name_in      = "Application.y_vs_i_vis_Trend1.1.sqlite"
select_frase    = "SELECT * from TblTrendData"
col_name_list   = np.array(["timestamp","y","i","N/A"])
select_list     = np.array([0,1,1,0])     
"""
# DF_csv.py:
# ----------
#path_csv        = r"C:\ProgramData\CODESYS\CODESYSControlWinV3x64\94BCBDE7\PlcLogic\trend\y_i_data.csv"
                       
# ------------------------------------------------------------

# #########################################################################################
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
        
"""       
# - imports df 
obj_ImportsqlitelDF  = ImportsqlitelDF ( db_name_in, select_frase, col_name_list, select_list) 
df                   = obj_ImportsqlitelDF.modify_df_of_ieee754_to_dec()

# - export to file.csv
obj_DFtoCSV = DFtoCSV(df, path_csv)
obj_DFtoCSV.exports_file_csv()
"""