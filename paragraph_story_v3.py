# paragraph_story_v1.py

# Purpose:
#   It creates the story for the file.pdf 
#   and it includes:
#   title, toc, plot tiles, text & images

# Packages:
import re
from datetime import datetime

#from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
from reportlab.lib.units import inch
from reportlab.lib.colors import red, orange, orangered,  green, darkcyan, blue, darkblue, darkslateblue, darkslategray, black
from reportlab.platypus import PageBreak
from reportlab.platypus import Image
from reportlab.platypus.paragraph import Paragraph
from reportlab.platypus.tableofcontents import TableOfContents

# import modules:
from text_in_to_list import FileInListConverter

# =================================================================================================================
class ParagraphTCOStory:

    def __init__(self, title_list, title_TOC_list, list_2d_in, size_char_list, line_splacer_list,font_type_list, 
        alignment_list, color_list, image_width_list, image_height_list):
        
        self.title_list           = title_list
        self.title_TOC_list       = title_TOC_list       
        self.list_2d_in           = list_2d_in
        self.size_char_list       = size_char_list
        self.line_splacer_list    = line_splacer_list
        self.font_type_list       = font_type_list
        self.alignment_list       = alignment_list
        self.color_list           = color_list
        self.image_width_list     = image_width_list
        self.image_height_list    = image_height_list
        
        # paragraph styles for different sections of the file
        # title pdf
        self.h0 = PS(name = 'title_pdf',
                fontSize = self.size_char_list[4],
                leading  = self.line_splacer_list[4],
                fontName = self.font_type_list[4],
                alignment= self.alignment_list[4],
                textColor= self.color_list[4])

        # title toc
        self.h1 = PS(name = 'title_TOC',
                fontSize = self.size_char_list[3],
                leading  = self.line_splacer_list[3],
                fontName = self.font_type_list[3],
                alignment= self.alignment_list[3],
                textColor= self.color_list[3])

        # main -> toc & title
        self.h2 = PS(name = 'Heading1',
                fontSize = self.size_char_list[2],
                leading  = self.line_splacer_list[2],
                fontName = self.font_type_list[2],
                alignment= self.alignment_list[2],
                textColor= self.color_list[2])
                
        # sub -> toc & plot_title
        self.h3 = PS(name = 'Heading2',
                fontSize = self.size_char_list[1],
                leading  = self.line_splacer_list[1],
                fontName = self.font_type_list[1],
                alignment= self.alignment_list[1],
                textColor= self.color_list[1])

        # body
        self.h4 = PS(name = 'body',
                fontSize = self.size_char_list[0],
                leading  = self.line_splacer_list[0],
                fontName = self.font_type_list[0],
                alignment= self.alignment_list[0],
                textColor= self.color_list[0])

    def bodyNimages(self):  
        
        Story = self.titleNtoc()

        # 2d list of images, text and headings
        for one_d_list in self.list_2d_in:

            for item in one_d_list:
                
                # when the item is an image
                if re.match ('\w.*png', item): 

                    Story.append(Paragraph('plot of the results', self.h3))
                    im = Image(item, 
                            self.image_width_list[0], 
                            self.image_height_list[0])

                    Story.append(im)
                    Story.append(PageBreak())

                # when the item is a file.txt
                if re.match ('\w.*txt', item): 

                    obj_FileInListConverter = FileInListConverter(item)
                    list_1d = obj_FileInListConverter.file_in_list_converter()

                    for elem in list_1d:
                        Story.append(Paragraph(elem, self.h4)) 

                    Story.append(PageBreak())

                # when the item is a string (this is the title of the plot N toc)
                if re.match ('^[^.]*$', item):
                    
                    if re.match ('Test: \w.*', item):
                        Story.append(Paragraph(item, self.h2))
                        
                    else:
                        Story.append(Paragraph(item, self.h3))

        return Story
            
        
    def titleNtoc(self):
            
        Story =[]

        # creates the tittle page
        for title in self.title_list:
                Story.append(Paragraph(title, self.h0))
        
        # starts a 2nd page after tittle
        Story.append(PageBreak())

        # creates the tittle TOC page
        for title in self.title_TOC_list:
            Story.append(Paragraph(title, self.h1))
            
        # initiates table of content
        toc = TableOfContents()
        toc.levelStyles = [self.h2, self.h3]

        # puts toc in to the Story
        Story.append(toc)
        Story.append(PageBreak())

        return Story
