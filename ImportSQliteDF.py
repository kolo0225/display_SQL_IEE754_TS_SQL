# ImportSQliteDF.py

# Purpose:
#       from sql.db creates pd.df 
#       by correcting selected values 
#       through the use of IEEE754_to_decimal.py

# Packages:
import numpy as np
import pandas as pd
import sqlite3
from time import strftime, localtime

# files.py
from IEEE754_to_decimal import IEEE754toDecimal

# ----------------------------------------------------------------
class ImportsqlitelDF:

    def __init__(self, db_name, select_frase, col_name_list, select_list): 

        # ------------ intializing results as empty values -----------
        df           = pd.DataFrame()

        # ------ instance variables ---------
        self.db_name            = db_name
        self.select_frase       = select_frase
        self.col_name_list      = col_name_list   
        self.select_list        = select_list
        
	# --------------------- Top Bottom design -------------------
	# creates a modified df with count instead of timestamp
    def modify_df_of_timestamp_to_count_sec(self):
       
        df           = self.modify_df_of_ieee754_to_dec()
        array_of_col = df.columns.to_numpy()
        
        col_array      = df[array_of_col[0]].to_numpy()
        col_array_time = np.array([])
       
        # --
        # if you want seconds rathter than TimeStamp
        # -------------------------------------------
        start_time     = col_array[0]/1e+6
        for index, val_time in enumerate(col_array):
             
            if index == 0:
                col_array_time = np.append(col_array_time, start_time/start_time)
            else:
                val_time = (val_time/1e+6) - start_time
                col_array_time = np.append(col_array_time, val_time)
        # -- 
        
        df[array_of_col[0]] = col_array_time
        #print(df[array_of_col[index]])
             
        return df 
    
    
    # creates a modified df with readable time instead of timestamp
    def modify_df_of_timestamp_to_time(self):
    
        df           = self.modify_df_of_ieee754_to_dec()
        array_of_col = df.columns.to_numpy()
        
        col_array      = df[array_of_col[0]].to_numpy()
        col_array_time = np.array([])
        
        # -
        # if you TimeStamp
        # -----------------
        for val_time in col_array:
           
            val_time = val_time/1e+6
            str_time = strftime('%Y-%m-%d %H:%M:%S', localtime(val_time))
            #print(str_time)
            col_array_time = np.append(col_array_time, str_time)
        # -
       
        df[array_of_col[0]] = col_array_time
        #print(df[array_of_col[index]])
             
        return df 
    
    
    # creates a modified df with decimal num instead of ieee754
    def modify_df_of_ieee754_to_dec(self):
    
        df           = self.rename_col_df()
        array_of_col = df.columns.to_numpy()
        
        for index, val in enumerate(self.select_list):
        
            if val == 1:
        
                col_array = df[array_of_col[index]].to_numpy()
                col_array_num = np.array([])
                
                for val_ieee754 in col_array:
                
                    val_ieee754 = str(val_ieee754)
                    
                    # --- to convert float num.0 to int num ---
                    if val_ieee754 != "nan":
                    
                        # -- remove the ".0" since pd is float
                        val_ieee754 = val_ieee754.replace(".0","")
                        val_ieee754 = int(val_ieee754)
                        # --
                        
                        # - call the IEEE754_to_decimal.py module
                        obj_IEEE754toDecimal    = IEEE754toDecimal(val_ieee754)
                        dec_num = obj_IEEE754toDecimal.fn_main()
                        col_array_num = np.append(col_array_num,dec_num)
                        # -
                    
                    else:
                        col_array_num = np.append(col_array_num,val_ieee754)
                    # ------------------------------------------- 
                
                df[array_of_col[index]] = col_array_num
                #print(df[array_of_col[index]])
                  
        return df 
    
    # rename columns 
    def rename_col_df(self):

        df = self.df_()

        df.drop(df.index[0])
        df.columns = self.col_name_list 

        return df 

    # df from file & table SQlite
    def df_ (self):
        
        conn = sqlite3.connect(self.db_name )
        print('Opened ', self.db_name,' database successfully',)
        
        df = pd.read_sql_query(self.select_frase, conn) 
        #df.replace(np.nan,0, inplace=True)
                            
        conn.close()

        return df
        
