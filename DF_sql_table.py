# DF_sql_table.py 

# Packages:

import numpy as np
import pandas as pd
import sqlite3

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

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
