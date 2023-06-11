# graph.py

# Purpose:
#   graphs oupts variables 
#   line diagram 
#       labeling (plots & axis)
#       colors of lines 

# Packages:
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt



#from ImportSQliteDF import ImportsqlitelDF
from graph_adjustments import GraphAdjustments

# ----------------- variables:
"""
# ImportSQliteDF:
# ---------------
db_name_in      = 'Application.RampRate_Trend1.1.sqlite'
select_frase    = 'SELECT * from TblTrendData'
col_name_list   = np.array(['timestamp','Spt','AutoSpt','FeedBack'])
select_list     = np.array([0,1,1,1]) 
# -
"""

# graph:
# ------
# colors
#color0    = 'springgreen'
#color1    = 'deepskyblue'
#color2    = 'deeppink'
#color3    = 'black'
#color4    = 'gold'
#color_list = np.array([color0,color1,color2,color3,color4])
# label
#label0    = 'Spt'
#label1    = 'AutoSpt'
#label2    = 'FeedBack'
#label_list = np.array([label0, label1, label2])
# label
#title     = 'Ramp Rate data over time'
#xlabel    = 'time'
#ylabel    = 'percent'
#title_list = np.array([title,xlabel,ylabel])
# graph adjusters
#round_num = 2
# list_lenght/divisor = num_display
#num_display = 20          # how mamy entries the x-axis will display for clarity
# output file.png
#output_graph_file = r'C:\Users\AE_Controls\Desktop\ramprate_test_data\ramp_rate_plot.png' 

"""
# ----------------- call classes
# - imports df 
obj_ImportsqlitelDF  = ImportsqlitelDF ( db_name_in, select_frase, col_name_list, select_list) 
#df             = obj_ImportsqlitelDF.modify_df_of_timestamp_to_time()             # choose time in timestamp
df             = obj_ImportsqlitelDF.modify_df_of_timestamp_to_count_sec()        # choose time in sec
"""
# ----------------------------------------

class Display:
    def __init__(self, df, color_list, label_list, title_list, round_num, num_display, output_graph_file):

        self.df                 = df
        self.color_list         = color_list
        self.label_list         = label_list
        self.title_list         = title_list
        self.round_num          = round_num
        # divisor = int(list_len/num_display)
        list_len = len(df.index.to_numpy())
        self.divisor = int(list_len/num_display)
        #self.divisor            = divisor
        self.output_graph_file  =output_graph_file
       
    # --------------------- Top Bottom design -------------------

    
    def x_val_based_on_TS_vals(self):  
        
        col_names = self.df.columns.to_numpy()
        
        # -
        # if you want TimeStamp or Sec
        # --------------------------------
        x_cord    = col_names[0]
        self.x    = self.df[x_cord].to_numpy()
        # -
        return self.x
        
        
    def x_val_based_on_index(self):     
       
        # --
        # if you want index
        # --------------------------------
        self.x    = self.df.index.to_numpy()
        # --
        return self.x
        
    
        
    def multiple_line_plots(self):
        
        col_names = self.df.columns.to_numpy()
        plot_num  = len(self.label_list)
        
        if plot_num == 1:
            # input y1
            y1_cord   = col_names[1]
            y1        = self.df[y1_cord].to_list()
            obj_GraphAdjustments = GraphAdjustments(y1,self.round_num,self.divisor)
            y1_list   = obj_GraphAdjustments.str_to_float_round()
            
            # plot line
            plt.plot(self.x, y1_list, color=self.color_list[0], label=self.label_list[0])

        if plot_num == 2:
            # input y1
            y1_cord   = col_names[1]
            y1        = self.df[y1_cord].to_list()
            obj_GraphAdjustments = GraphAdjustments(y1,self.round_num,self.divisor)
            y1_list   = obj_GraphAdjustments.str_to_float_round()
            
            # input y2
            y2_cord   = col_names[2]
            y2        = self.df[y2_cord].to_list()
            obj_GraphAdjustments = GraphAdjustments(y2,self.round_num,self.divisor)
            y2_list   = obj_GraphAdjustments.str_to_float_round()
         
            # plot line
            plt.plot(self.x, y1_list, color=self.color_list[0], label=self.label_list[0])
            plt.plot(self.x, y2_list, color=self.color_list[1], label=self.label_list[1])
            
        if plot_num == 3:
            # input y1
            y1_cord   = col_names[1]
            y1        = self.df[y1_cord].to_list()
            obj_GraphAdjustments = GraphAdjustments(y1,self.round_num,self.divisor)
            y1_list   = obj_GraphAdjustments.str_to_float_round()
            
            # input y2
            y2_cord   = col_names[2]
            y2        = self.df[y2_cord].to_list()
            obj_GraphAdjustments = GraphAdjustments(y2,self.round_num,self.divisor)
            y2_list   = obj_GraphAdjustments.str_to_float_round()
         
            # input y3
            y3_cord   = col_names[3]
            y3        = self.df[y3_cord].to_list()
            obj_GraphAdjustments = GraphAdjustments(y3,self.round_num,self.divisor)
            y3_list   = obj_GraphAdjustments.str_to_float_round()
            
            # plot line
            plt.plot(self.x, y1_list, color=self.color_list[0], label=self.label_list[0])
            plt.plot(self.x, y2_list, color=self.color_list[1], label=self.label_list[1])
            plt.plot(self.x, y3_list, color=self.color_list[2], label=self.label_list[2])
            
        if plot_num == 4:
            # input y1
            y1_cord   = col_names[1]
            y1        = self.df[y1_cord].to_list()
            obj_GraphAdjustments = GraphAdjustments(y1,self.round_num,self.divisor)
            y1_list   = obj_GraphAdjustments.str_to_float_round()
            
            # input y2
            y2_cord   = col_names[2]
            y2        = self.df[y2_cord].to_list()
            obj_GraphAdjustments = GraphAdjustments(y2,self.round_num,self.divisor)
            y2_list   = obj_GraphAdjustments.str_to_float_round()
         
            # input y3
            y3_cord   = col_names[3]
            y3        = self.df[y3_cord].to_list()
            obj_GraphAdjustments = GraphAdjustments(y3,self.round_num,self.divisor)
            y3_list   = obj_GraphAdjustments.str_to_float_round()
            
            # input y4
            y4_cord   = col_names[4]
            y4        = self.df[y4_cord].to_numpy()
            obj_GraphAdjustments = GraphAdjustments(y4,self.round_num,self.divisor)
            y4_list   = obj_GraphAdjustments.str_to_float_round()
            
            # plot line
            plt.plot(self.x, y1_list, color=self.color_list[0], label=self.label_list[0])
            plt.plot(self.x, y2_list, color=self.color_list[1], label=self.label_list[1])
            plt.plot(self.x, y3_list, color=self.color_list[2], label=self.label_list[2])
            plt.plot(self.x, y4_list, color=self.color_list[3], label=self.label_list[3])
           
        if plot_num == 5:
            # input y1
            y1_cord   = col_names[1]
            y1        = self.df[y1_cord].to_list()
            obj_GraphAdjustments = GraphAdjustments(y1,self.round_num,self.divisor)
            y1_list   = obj_GraphAdjustments.str_to_float_round()
            
            # input y2
            y2_cord   = col_names[2]
            y2        = self.df[y2_cord].to_list()
            obj_GraphAdjustments = GraphAdjustments(y2,self.round_num,self.divisor)
            y2_list   = obj_GraphAdjustments.str_to_float_round()
         
            # input y3
            y3_cord   = col_names[3]
            y3        = self.df[y3_cord].to_list()
            obj_GraphAdjustments = GraphAdjustments(y3,self.round_num,self.divisor)
            y3_list   = obj_GraphAdjustments.str_to_float_round()
            
            # input y4
            y4_cord   = col_names[4]
            y4        = self.df[y4_cord].to_numpy()
            obj_GraphAdjustments = GraphAdjustments(y4,self.round_num,self.divisor)
            y4_list   = obj_GraphAdjustments.str_to_float_round()
            
            # input y5
            y5_cord   = col_names[5]
            y5        = self.df[y5_cord].to_numpy()
            obj_GraphAdjustments = GraphAdjustments(y5,self.round_num,self.divisor)
            y5_list   = obj_GraphAdjustments.str_to_float_round()
            
            # plot line
            plt.plot(self.x, y1_list, color=self.color_list[0], label=self.label_list[0])
            plt.plot(self.x, y2_list, color=self.color_list[1], label=self.label_list[1])
            plt.plot(self.x, y3_list, color=self.color_list[2], label=self.label_list[2])
            plt.plot(self.x, y4_list, color=self.color_list[3], label=self.label_list[3])
            plt.plot(self.x, y5_list, color=self.color_list[4], label=self.label_list[4])
           
       
        else:
            print( "you enter too many plots")
        
        # ================= plot ======================
        
        # labeling 
        plt.xlabel(self.title_list[1], fontsize=15)
        plt.ylabel(self.title_list[2], fontsize=15)
        plt.title(self.title_list[0], fontsize=15)  
        
        # plot parameters
        obj_GraphAdjustments = GraphAdjustments(self.x,self.round_num,self.divisor)
        x_reduced            = obj_GraphAdjustments.reduce_list_len()
        
        plt.xticks(rotation=45)
        plt.xticks(x_reduced)
        plt.legend()
        
        # save fig
        plt.savefig(self.output_graph_file)
        
        # show and close
        #plt.show()
        plt.close()
        # ============================================

"""
# multigraph 
obj_Display = Display(df, color_list, label_list, title_list, round_num, num_display, output_graph_file)
#obj_Display.x_val_based_on_TS_vals()                    # x in sec or TS
obj_Display.x_val_based_on_index()                      # x in cycles
obj_Display.multiple_line_plots()
"""
