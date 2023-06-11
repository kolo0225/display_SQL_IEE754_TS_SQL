# main_RampRate_cleaner.py 

# Purpose:
#       main function is there to call all classes needed 
#       for clean and repopulate sqlite 

# Packages:
import os 
import sys
import subprocess
import time
from datetime import datetime
import numpy as np
import pandas as pd
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch              # (8.5* inch, 11 * inch)
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.colors import blue, green, red, black



# files.py
from ImportSQliteDF import ImportsqlitelDF
from DF_csv import DFtoCSV
from DF_sql_table import DfSqlTable
from graph import Display
from text_to_pdf_v2 import TextProcessorToPDF
from DirectoriesControl import DirectoryFileManager


# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# Varibles need CHANGE @ ONLY ONCE:
#----------------------------------
# ----------------- variables:
# NOTE:
# The file "sftp_downloading_RampRate_files.ps1"
#   need to be change for each test case
# the 2 variables (from powershell) below 
#   you can only change them from "sftp_downloading_RampRate_files.ps1"

# ---> sftp_downloading_RampRate_files.ps1
# $linux_file  = '/var/opt/codesys/PlcLogic/trend/Application.RampRate_Trend1.1.sqlite'
# $win_path    = 'C:\Users\AE_Controls\Desktop\ramprate_test_data'
# name of //sftp_downloading_*******_files.ps1" 
# NOTE: both files.ps1 have to be at the same directory
dir_pwsh         = os.getcwd()                                                   # NEVER CHANGE
file_ps1_1       = "\\sftp_downloading_RampRate_files.ps1"        
# --------------------------------------------------------------

# delay variable to insure sqlite has been imported
delay = 5; # sec                                               # NEVER CHANGE

# ---> ImportSQliteDF:
#      ---------------
db_name_in      = 'Application.RampRate_Trend1.1.sqlite'       
select_frase    = 'SELECT * from TblTrendData'                # Do not need to change
col_name_list   = np.array(['timestamp','Spt','AutoSpt','FeedBack'])   # name columns   
select_list     = np.array([0,1,1,1])                                  # if 1 column will be IEEE754 -> float

# ---> DF_csv:
#      ----------
path_csv        = 'RampRate_data.csv'

# ---> DF_sql_table:
#      -------------
db_name_out       = 'corrected_RampRate_data.sqlite'
table_name        = 'TblTrendData'                               # NEVER CHANGE
# only change the column names (keep them the same as "col_name_list" above)
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

# ---> graph:
#      ------
# colors                                                       # NEVER CHANGE              
color0    = 'springgreen'
color1    = 'deepskyblue'
color2    = 'deeppink'
color3    = 'black'
color4    = 'gold'
color_list_plot = np.array([color0,color1,color2,color3,color4])  
# label                      # select names you want to give to your lines ploted 
label0    = 'Spt'
label1    = 'AutoSpt'
label2    = 'FeedBack'
label_list_plot = np.array([label0, label1, label2])
# label                    # label plot and axis
title     = 'Ramp Rate data over time'
xlabel    = 'time [sec]'
ylabel    = 'percent [%]'
title_list_plot = np.array([title,xlabel,ylabel])
# graph adjusters
round_num = 2                                                                     # NEVER CHANGE              
# list_lenght/divisor = num_display
num_display = 20          # how mamy entries the x-axis will display for clarity  # NEVER CHANGE 
# output file.png
output_graph_file = 'ramp_rate_plot.png'   

# ---> text_to_pdf
#      -----------
# files want to add in the result page:
current_date = datetime.now()
date_str     = current_date.strftime('%m/%d/%y %H:%M:%S')

#                               Write Files

# 'title_file.txt'
# This file name for title SHOULD NOT CHANGES
title_list = ['title_file.txt', 
                '',
                '*******************************',
                'Test: Temp_Real Power Ramp Rate',
                 date_str,
                 '*******************************',
                '']
           
# Note:
#   Name the file as *title_img.txt if this is a title for a plot. 
#       This will denerate a new page that the title and the image will be placed at:
#       in 'list_file_in' place '*title_img.txt' right in from of '\w.*png'
# 'plot_res_intro'
plot_res_intro_list = ['plot_res_title_img.txt', 
                '',
                'Plot of Test:',
                '------------------',
                '']
    
# variables
files_to_write_list = [title_list, plot_res_intro_list]

list_file_in        = ['title_file.txt','RampUpDownTestDoc.txt', 'RampUpDownStopwatch.log',
                       'plot_res_title_img.txt', 'ramp_rate_plot.png']

output_file_pdf     = 'RampRateTestResults.pdf'

# varibles on pdf apperance:
# size of text
size_text_char       = 10
size_plot_text_char  = 14
size_title_text_char = 20
size_char_list = [size_text_char,size_plot_text_char,size_title_text_char ]
# font type
font_type_text       = "Helvetica"
font_type_plot_text  = "Times-Bold"
font_type_title_text = "Times-Bold"
font_type_list = [font_type_text, font_type_plot_text, font_type_title_text]
# font color
color_text       = blue
color_plot_text  = green
color_title_text = black
color_list = [color_text, color_plot_text, color_title_text]

# text (from the left)
text_position_L    = 1 * inch
plot_position_L    = 3 * inch
title_position_L   = 2 * inch
text_position_list_L = [text_position_L, plot_position_L, title_position_L]
# text (from the bottom)
text_position_B    = 10 * inch 
plot_position_B    = 10 * inch 
title_position_B   = 10 * inch 
text_position_list_B = [text_position_B, plot_position_B, title_position_B]

line_splacer_text       = 0.5
line_splacer_plot_text  = 0.5
line_splacer_title_text = 0.5
line_splacer_list = [line_splacer_text,line_splacer_plot_text, line_splacer_title_text]


# image parameters 
# position (from the left)
x_plot_image   = 1 * inch
x_image_list   = [x_plot_image]
# (from the bottom)
y_plot_image   = 3 * inch
y_image_list   = [y_plot_image]

# size
# width 
image_plot_width  = 6 * inch
image_width_list  = [image_plot_width]
# height
image_plot_height  = 6 * inch
image_height_list  = [image_plot_height]


# ---> DirectoriesControl
dir_name             = '\\RampRateTest_'
list_tobe_copied     = ['RampRate_data.csv', 'corrected_RampRate_data.sqlite', 'RampRateTestResults.pdf', 'PRealRampRataIncrDecrTest.html']
list_tobe_invoked    = ['RampRateTestResults.pdf', 'PRealRampRataIncrDecrTest.html']

# --------------------------------------------------------------
# NOTE:
# The file "sftp_ls_RampRate_sqliteDeleter.ps1"
#   need to be change for each test case
# the variable (from powershell) below 
#   you can only change them from "sftp_ls_RampRate_sqliteDeleter.ps1"
# name of //sftp_ls_*******_sqliteDeleter.ps1" 
file_ps1_2       = "\\sftp_ls_RampRate_sqliteDeleter.ps1"  
# --------------------------------------------------------------
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# ########################################################################################
# ----------------- call classes
"""
# powershell files "sftp_downloading_RampRate_files.ps1"
# file -> should should be different for each test case
pwsh_path_file_1 = dir_pwsh+file_ps1_1
subprocess.Popen(["powershell.exe",pwsh_path_file_1], stdout=sys.stdout)         

# add a delay to insure sqlite is imported
time.sleep(delay)
"""
# - imports df 
obj_ImportsqlitelDF  = ImportsqlitelDF ( db_name_in, select_frase, col_name_list, select_list) 
df_ts             = obj_ImportsqlitelDF.modify_df_of_timestamp_to_time()             # choose time in timestamp (use both)
df_sec            = obj_ImportsqlitelDF.modify_df_of_timestamp_to_count_sec()        # choose time in sec (use both)
# ---

# - export to file.csv
obj_DFtoCSV = DFtoCSV(df_ts, path_csv)
obj_DFtoCSV.exports_file_csv()
# -

# ---
# - DF_sql_table
obj_DfSqlTable  = DfSqlTable (db_name_out, table_name, table_str, df_ts, drop_str, view )  

#obj_DfSqlTable.create_connect_db()
obj_DfSqlTable.create_table_populate()
#obj_DfSqlTable.view_db()
# -

# ---
# graph 
obj_Display = Display(df_sec, color_list_plot, label_list_plot, title_list_plot, round_num, num_display,output_graph_file)
obj_Display.x_val_based_on_TS_vals()          # x in seconds
#obj_Display.x_val_based_on_index()             # x in cycles
obj_Display.multiple_line_plots()
# -

# ---
# text_to_pdf
obj_TextProcessorToPDF  = TextProcessorToPDF(files_to_write_list, list_file_in, size_char_list, font_type_list, 
        color_list, text_position_list_L, text_position_list_B, line_splacer_list, 
        x_image_list, y_image_list, image_width_list, image_height_list, output_file_pdf)
                                                
obj_TextProcessorToPDF.file_writer()
obj_TextProcessorToPDF.main_creates_pdf()
# -

# ---
# DirectoriesControl
obj_DirectoryFileManager = DirectoryFileManager(dir_name, list_tobe_copied, list_tobe_invoked) 
obj_DirectoryFileManager.invoke_files_selected()
obj_DirectoryFileManager.zip_directory()
# -
"""
# ---
# powershell files "sftp_ls_RampRate_sqliteDeleter.ps1"
# file -> should should be different for each test case
pwsh_path_file_2 = dir_pwsh+file_ps1_2
subprocess.Popen(["powershell.exe",pwsh_path_file_2], stdout=sys.stdout)         # NEVER CHANGE
"""
# ----------------- Display 

pd.options.display.float_format = '{:.0f}'.format
print (df_ts.shape)
print (df_ts.columns)
print (df_ts.head(20))
print (df_ts.tail(10))
#print (df.describe())
