# text_to_pdf_v2.py

# Purpose: 
#   Combines files.txt 
#   trnsforms them in to PDF

# Packages:
import re
from datetime import datetime
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch              # (8.5* inch, 11 * inch)
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.colors import blue, green, red, black
"""
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

output_file_pdf     = 'temp_RampRateTestResults.pdf'

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

"""
class TextProcessorToPDF: 

    def __init__(self, files_to_write_list, list_file_in, size_char_list, font_type_list, 
        color_list, text_position_list_L, text_position_list_B, line_splacer_list,
        x_image_list, y_image_list, image_width_list, image_height_list, output_file_pdf):
        
        self.files_to_write_list  = files_to_write_list
        self.list_file_in         = list_file_in
        self.size_char_list       = size_char_list
        self.font_type_list       = font_type_list
        self.color_list           = color_list
        self.text_position_list_L = text_position_list_L
        self.text_position_list_B = text_position_list_B
        self.line_splacer_list    = line_splacer_list
        self.x_image_list         = x_image_list
        self.y_image_list         = y_image_list
        self.image_width_list     = image_width_list
        self.image_height_list    = image_height_list
        self.output_file_pdf      = output_file_pdf
    
   
    def main_creates_pdf(self):
        
        canvas = Canvas(self.output_file_pdf, pagesize=LETTER)           # creates the file.pdf 8.5*11
        
        # if name = *.html it adds image
        for file in self.list_file_in:
            
            # if name = *.png it adds image
            if re.match ('\w.*png' , file): 
               
                # image -> pdf function (for the plot)
                canvas = self.image_plot_to_pdf(canvas, file)
            
            # The name of the title file should never change
            elif re.match ('title_file.txt', file):
                
                # text_file_title -> pdf function
                canvas = self.file_title_text_to_pdf(canvas, file)
                
            # if name = *title_img.txt add a title
            elif re.match ('\w.*title_img.txt', file):
                
                # text_plot_title -> pdf function 
                canvas = self.plot_title_text_to_pdf(canvas, file)
                
            # Adds the rest of the txt body
            else:
                
                # call text to pdf function         
                canvas = self.text_to_pdf(canvas, file)
            
        canvas.save()
        
        return
    
       
    # image plot -> pdf function 
    def  image_plot_to_pdf(self, canvas, file):
        
        canvas.drawImage(file, self.x_image_list[0], self.y_image_list[0], width=self.image_width_list[0], height=self.image_height_list[0])
        
        return canvas
    
    # text_file_title -> pdf function 
    def file_title_text_to_pdf(self, canvas, file):
        
        # call basic cell of text to pdf function         
        canvas = self.text_to_pdf_cell(canvas, file, self.line_splacer_list[2], self.font_type_list[2], self.size_char_list[2], 
                            self.color_list[2], self.text_position_list_L[2], self.text_position_list_B[2])
        
        canvas.showPage()
        
        return  canvas   
    
    # text_plot_title -> pdf function 
    def plot_title_text_to_pdf(self, canvas, file):
        
        # call basic cell of text to pdf function         
        canvas = self.text_to_pdf_cell(canvas, file, self.line_splacer_list[1], self.font_type_list[1], self.size_char_list[1], 
                            self.color_list[1], self.text_position_list_L[1], self.text_position_list_B[1])
        
        return  canvas
   

    # text -> pdf function 
    def text_to_pdf(self, canvas, file):
        
        # call basic cell of text to pdf function         
        canvas = self.text_to_pdf_cell(canvas, file, self.line_splacer_list[0], self.font_type_list[0], self.size_char_list[0], 
                            self.color_list[0], self.text_position_list_L[0], self.text_position_list_B[0])
        
        canvas.showPage()
        
        return canvas
     
     
    # basic cell of text to pdf function   
    def text_to_pdf_cell(self, canvas, file, line_splacer, font_type, font_Size, color_text, text_position_L, text_position_B):
        
        line_down = 0
        index_equivalent       = 0
        with open(file, 'r') as r:
            content = r.read()
            
            for index, line in enumerate(content.splitlines()):
                
                canvas.setFont(font_type, font_Size)
                canvas.setFillColor(color_text)
                
                # removes weird characters that appear in the pdf (and spaces)
                line = line.strip()
                
                line_down = (index-index_equivalent)*(inch*line_splacer)
                
                if (line_down > 680):
                    
                    index_equivalent = index
                    line_down        = (index-index_equivalent)*(inch*line_splacer)
                    
                    canvas.showPage()
                    canvas.setFont(font_type, font_Size)
                    canvas.setFillColor(color_text)
                    
                    canvas.drawString(text_position_L, text_position_B-line_down, line) # 72,72 = location of that text is written form L & from bottom
                    
                else:
                    canvas.drawString(text_position_L, text_position_B-line_down, line) # 72,72 = location of that text is written form L & from bottom
                 
        return canvas
   
    # creates a document file.txt
    def file_writer(self):
        
        for file in self.files_to_write_list:
        
            for index,line in enumerate(file):
                
                file_name = file[0]
                
                if index ==0:
                    with open(file_name, 'w') as w:
                        w.write('')
                else:
                    with open(file_name, 'a') as a:
                        a.write(line)
                        a.write('\n')
            
        return
        
    
"""
obj_TextProcessorToPDF  = TextProcessorToPDF(files_to_write_list, list_file_in, size_char_list, font_type_list, 
        color_list, text_position_list_L, text_position_list_B, line_splacer_list, 
        x_image_list, y_image_list, image_width_list, image_height_list, output_file_pdf)
                                                
obj_TextProcessorToPDF.file_writer()
obj_TextProcessorToPDF.main_creates_pdf()
"""
