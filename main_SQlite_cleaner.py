# main_SQlite_cleaner.py 

# Purpose:
#       main function is there to call all classes needed 
#       for clean and repopulate sqlite 

# Packages:
import numpy as np
import pandas as pd
import sqlite3 

# files.py
from ImportSQliteDF import ImportsqlitelDF
from DF_csv import DFtoCSV
from DF_sql_table import DfSqlTable
from graph import Display

# ----------------- variables:
# ImportSQliteDF:
# ---------------
db_name_in      = "Application.y_vs_i_vis_Trend1.1.sqlite"
select_frase    = "SELECT * from TblTrendData"
col_name_list   = np.array(["timestamp","y","i","N/A"])
select_list     = np.array([0,1,1,0]) 

# DF_csv.py:
# ----------
path_csv        = r"C:\ProgramData\CODESYS\CODESYSControlWinV3x64\94BCBDE7\PlcLogic\trend\y_i_data.csv"

# DF_sql_table:
# -------------
db_name_out       = "corrected_y_i_data.sqlite"
table_name        = "TblTrendData"
table_str         = '''CREATE TABLE IF NOT EXISTS TblTrendData( 
		               timestamp INTEGER PRIMARY KEY,
		               y REAL,
                       i REAL
	                  );''' 
drop_str          = "drop table if exists TblTrendData"

view              = ('''  
	                  SELECT * FROM TblTrendData
                    ''')

# graph:
# ------
# colors
color0 ="deeppink"
color1 ="deepskyblue"
color_list = np.array([color0,color1])
# label
label0 = "y"
label1 = "i"
label_list = np.array([label0, label1])
# label
title  = "data over time"
xlabel = "time"
ylabes = "data"
title_list = np.array([title,xlabel,ylabes])


# ----------------- call classes

# - imports df 
obj_ImportsqlitelDF  = ImportsqlitelDF ( db_name_in, select_frase, col_name_list, select_list) 
df             = obj_ImportsqlitelDF.modify_df_of_timestamp_to_time()
# ---
# - export to file.csv
obj_DFtoCSV = DFtoCSV(df, path_csv)
obj_DFtoCSV.exports_file_csv()
# -

# ---
# - DF_sql_table
obj_DfSqlTable  = DfSqlTable (db_name_out, table_name, table_str, df, drop_str, view )  

#obj_DfSqlTable.create_connect_db()
obj_DfSqlTable.create_table_populate()
#obj_DfSqlTable.view_db()

# ---
# - graph
obj_Display = Display(df, color_list, label_list, title_list)
obj_Display.multiple_line_plots()

"""
# ----------------- Display 

pd.options.display.float_format = '{:.0f}'.format
print (df.shape)
print (df.columns)
print (df.head(5))
print (df.tail(5))
print (df.describe())
"""