# DF_sql_table.py 

# Packages:

import numpy as np
import pandas as pd
import sqlite3
"""
# files.py
from ImportSQliteDF import ImportsqlitelDF
"""
# path
#r"C:\ProgramData\CODESYS\CODESYSControlWinV3x64\94BCBDE7\PlcLogic\corrected***.sqlite"         

# ####################################### universal variables #############################
#

# ------------- TEMP - ImportSQliteDF.py - VAR.---------- 
"""
# ----------------- variables:
# ImportSQliteDF:
# ---------------
db_name_in      = 'Application.RampRate_Trend1.1.sqlite'
select_frase    = 'SELECT * from TblTrendData'
col_name_list   = np.array(['timestamp','Spt','AutoSpt','FeedBack'])
select_list     = np.array([0,1,1,1]) 

# ------------------------------------------------------------
# DF_sql_table:
# ---------------

db_name_out       = 'corrected_RampRate_data.sqlite'
table_name        = 'TblTrendData'                               # NEVER CHANGE
table_str         = '''CREATE TABLE IF NOT EXISTS TblTrendData( 
		               timestamp INTEGER PRIMARY KEY,
		               Spt REAL,
                       AutoSpt REAL,
                       FeedBack REAL 
	                  );''' 
drop_str          = 'drop table if exists TblTrendData'         # NEVER CHANGE

view              = ('''  
	                  SELECT * FROM TblTrendData                # NEVER CHANGE
                    ''')
"""
# ------------------------------------------------------------

# #########################################################################################
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# ----------------------------------------------------------------
"""<-----------------|Start Comment|
"""# <-----------------|End Comment|
# b: DfSqlTable:

class DfSqlTable: 

    # ------------ intializing results as empty values -----------
            
    def __init__(self,  db_name, table_name, table_str, df, drop_str, view): 

        # ------ instance variables ---------
        self.db_name           = db_name
        self.table_name        = table_name
        self.table_str         = table_str
        self.df                = df
        self.drop_str          = drop_str
        self.view              = view
    
    # --------------------- Top Bottom design -------------------
   
    def view_db(self):

        conn = sqlite3.connect(self.db_name )
        
        c = conn.cursor()
        c.execute(self.view)

        for row in c.fetchall():
            print (row)
        
        conn.close()	

    # db & table in this fn    
    def create_table_populate(self):

        conn = sqlite3.connect(self.db_name )

        c = conn.cursor()		

        c.execute(self.drop_str)

        table = c.execute(self.table_str)
        print('table ', self.table_name, ' is ready')

        self.df.to_sql(self.table_name, conn, if_exists="replace")
        print('table is populated with data')

        conn.commit()
        conn.close()

        return table
        
  
    # -----------------------------------------
    # these functions are called by fns above:

    # Connect/create To Database:
    def create_connect_db (self):

        conn = sqlite3.connect(self.db_name )
        print('Opened ', self.db_name,' database successfully')

        conn.close()

#--------------------------------------------------------
"""
# ==========> imports df 
# - imports df 
obj_ImportsqlitelDF  = ImportsqlitelDF ( db_name_in, select_frase, col_name_list, select_list) 
df             = obj_ImportsqlitelDF.modify_df_of_timestamp_to_time()             # choose time in timestamp
#df            = obj_ImportsqlitelDF.modify_df_of_timestamp_to_count_sec()         # choose time in sec


# ==========> 1b DfSqlTable
obj_DfSqlTable  = DfSqlTable (db_name_out, table_name, table_str, df, drop_str, view )  

#obj_DfSqlTable.create_connect_db()
obj_DfSqlTable.create_table_populate()
#obj_DfSqlTable.view_db()
"""
