# graph.py

# Purpose:
#   graphs oupts variables 

# Packages:
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt


# files.py
"""
from ImportSQliteDF import ImportsqlitelDF

# ----------------- variables:
# ImportSQliteDF:
# ---------------
db_name_in      = "Application.y_vs_i_vis_Trend1.1.sqlite"
select_frase    = "SELECT * from TblTrendData"
col_name_list   = np.array(["timestamp","y","i","N/A"])
select_list     = np.array([0,1,1,0]) 
# -
"""
"""
# graph:
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
"""
# ----------------- call classes
"""
# - imports df 
obj_ImportsqlitelDF  = ImportsqlitelDF ( db_name_in, select_frase, col_name_list, select_list) 
df             = obj_ImportsqlitelDF.modify_df_of_timestamp_to_time()
"""

# ----------------------------------------

class Display:
    def __init__(self, df, color_list, label_list, title_list):

        self.df               = df
        self.color_list       = color_list
        self.label_list       = label_list
        self.title_list       = title_list

    # --------------------- Top Bottom design -------------------

    def multiple_line_plots(self):
        
        
        
        col_names = self.df.columns.to_numpy()
        
        # df columns in to np.arrays
        # x-value 
        x_cord    = col_names[0]
        x         = self.df[x_cord].to_numpy()

        # input y
        y1_cord   = col_names[1]
        y1        = self.df[y1_cord].to_numpy()

        # input i
        y2_cord   = col_names[2]
        y2        = self.df[y2_cord].to_numpy()
       
        # ================= plot ======================
        # limit @ x-axis
        
        #labeling 
        plt.xlabel(self.title_list[1], fontsize=15)
        plt.ylabel(self.title_list[2], fontsize=15)
        plt.title(self.title_list[0], fontsize=15)

        # plot line
        plt.plot(x, y1, color=self.color_list[0], label=self.label_list[0])
        plt.plot(x, y2, color=self.color_list[1], label=self.label_list[1])
       
        plt.xticks(rotation=45)
        plt.legend()
        plt.show()
        # ============================================

"""
# multigraph 
obj_Display = Display(df, color_list, label_list, title_list)
obj_Display.multiple_line_plots()
"""