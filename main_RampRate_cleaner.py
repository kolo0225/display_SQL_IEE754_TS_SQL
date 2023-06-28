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
from reportlab.lib.colors import red, orange, orangered,  green, darkcyan, blue, darkblue, darkslateblue, darkslategray, black
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY




# files.py
from ImportSQliteDF import ImportsqlitelDF
from DF_csv import DFtoCSV
from DF_sql_table import DfSqlTable
from graph import Display
from paragraph_story_v3 import ParagraphTCOStory
from build_pdf_v4 import PDF_Buider
from DirectoriesControl import DirectoryFileManager


# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# Varibles need CHANGE @ ONLY ONCE:
#----------------------------------
# ----------------- variables:

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

# ---> paragraph_story
#      -----------
# date time for title_pdf
current_date = datetime.now()
date_str     = current_date.strftime('%m/%d/%y %H:%M:%S')

# title -> this is a separtate input list
title0 =  'The Result of all Tests:'
title1 =  date_str
title_list = [title0, title1]

# title TOC
title0 =  'Table of Contents'
title_TOC_list = [title0]

# string and files.txt -> 1st list in list_2d_in
text0 =  'Test: Preal Ramp Rate'                 # Each Test should start with 'Test: '
text1 =  'These are the parameters of the test'
text2 =  'RampUpDownTestDoc.txt'
text3 =  'time logs for the Preal Ramp test'
text4 =  'RampUpDownStopwatch.txt'
text_list = [text0, text1, text2, text3, text4]
# image -> 2nd list in list_2d_in
image0  = 'ramp_rate_plot.png'
image_list = [image0]

# 2d image and strings/file.txt
list_2d_in  = [text_list, image_list]

# varibles on pdf apperance:
# size of text
size_text_char       = 12
size_plot_sub_char   = 14
size_plot_main_char  = 18
size_title_TOC_char  = 20
size_title_text_char = 20
size_char_list = [size_text_char, size_plot_sub_char, size_plot_main_char, size_title_TOC_char, size_title_text_char ]
# line spacer (fonr_size <= spacer)
line_splacer_text       = 20
line_splacer_plot_sub   = 20
line_splacer_plot_main  = 20
line_splacer_TOC_text   = 24
line_splacer_title_text = 40
line_splacer_list = [line_splacer_text, line_splacer_plot_sub, line_splacer_plot_main, line_splacer_TOC_text, line_splacer_title_text]
# font type
font_type_text       = 'Helvetica'
font_type_plot_sub   = 'Courier'
font_type_plot_main  = 'Courier'
font_type_TOC_text   = 'Times'
font_type_title_text = 'Times-Bold'
font_type_list = [font_type_text, font_type_plot_sub, font_type_plot_main, font_type_TOC_text, font_type_title_text]
# font color
color_text       = black
color_plot_sub   = black
color_plot_main  = black
color_TOC_text   = darkslategray
color_title_text = darkslategray
color_list = [color_text, color_plot_sub, color_plot_main, color_TOC_text, color_title_text]
# alignment 
alignment_text       = TA_LEFT
alignment_plot_sub   = TA_LEFT
alignment_plot_main  = TA_LEFT
alignment_TOC_text   = TA_LEFT
alignment_title_text = TA_CENTER
alignment_list = [alignment_text, alignment_plot_sub, alignment_plot_main, alignment_TOC_text, alignment_title_text]

# image parameters 
# size
# width 
image_plot_width  = 6 * inch
image_width_list  = [image_plot_width]
# height
image_plot_height  = 6 * inch
image_height_list  = [image_plot_height]

# ---> build_pdf
#      -----------
file_out = 'RampRateTestResults.pdf'

# ---> DirectoriesControl
dir_name             = '\\RampRateTest_'
list_tobe_copied     = ['RampRate_data.csv', 'corrected_RampRate_data.sqlite', 'RampRateTestResults.pdf', 'PRealRampRataIncrDecrTest.html']
list_tobe_invoked    = ['RampRateTestResults.pdf', 'PRealRampRataIncrDecrTest.html']

# ########################################################################################
# ----------------- call classes

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
# paragraph_story
obj_ParagraphTCOStory = ParagraphTCOStory( title_list, title_TOC_list, list_2d_in, size_char_list, 
        line_splacer_list,font_type_list, alignment_list, color_list, image_width_list, image_height_list)

Story = obj_ParagraphTCOStory.bodyNimages()
# -

# ---
# buid_pdf
obj_PDF_Buider = PDF_Buider(file_out)
doc = obj_PDF_Buider.multiBuild(Story)
# -

"""
# uncomment if you wish to create a TimeStamp_file with the results in
# ---
# DirectoriesControl
obj_DirectoryFileManager = DirectoryFileManager(dir_name, list_tobe_copied, list_tobe_invoked)
obj_DirectoryFileManager.invoke_files_selected()
obj_DirectoryFileManager.zip_directory()
# -
"""
# ----------------- Display 

pd.options.display.float_format = '{:.0f}'.format
print (df_ts.shape)
print (df_ts.columns)
print (df_ts.head(20))
print (df_ts.tail(10))
