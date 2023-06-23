# build_pdf_v4.py

# import modules:
"""
from text_in_to_list import FileInListConverter
from paragraph_story_v3 import ParagraphTCOStory
"""
from header_n_footer_v1 import combine_header_footer  # uncommented
"""

# packages
# Need for the paragraph_story
import re
from datetime import datetime
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
from reportlab.lib.units import inch
from reportlab.lib.colors import red, orange, orangered,  green, darkcyan, blue, darkblue, darkslateblue, darkslategray, black

# variables:
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


# create and call obj
obj_ParagraphTCOStory = ParagraphTCOStory( title_list, title_TOC_list, list_2d_in, size_char_list, 
        line_splacer_list,font_type_list, alignment_list, color_list, image_width_list, image_height_list)

Story = obj_ParagraphTCOStory.bodyNimages()
"""
# Packages:
# Need for the build_pdf
#from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus.paragraph import Paragraph
from reportlab.platypus.doctemplate import PageTemplate, BaseDocTemplate
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.platypus.frames import Frame
from functools import partial
"""
# variables:
file_out = 'temp_table_of_content_v3.pdf'
"""
class PDF_Buider(BaseDocTemplate):
    
    def __init__(self, file_out, **kw):
        
       
        self.allowSplitting = 0
        BaseDocTemplate.__init__(self, file_out, **kw)
        frame = Frame(1*inch, 1*inch, 6*inch, 10*inch, id='F1')
        template = PageTemplate('normal', frame, onPage=partial(combine_header_footer))
        self.addPageTemplates(template)
        
    def afterFlowable(self, flowable):
        
        if flowable.__class__.__name__ == 'Paragraph':
            text = flowable.getPlainText()
            style = flowable.style.name
              
            if style == 'Heading1':
                key = 'h2-%s' % self.seq.nextf('Heading1')
                self.canv.bookmarkPage(key)
                self.notify('TOCEntry', (0, text, self.page, key))
                
            elif style == 'Heading2':
                key = 'h3-%s' % self.seq.nextf('Heading2')
                self.canv.bookmarkPage(key)
                self.notify('TOCEntry', (2, text, self.page, key))

"""
# create and call obj
obj_PDF_Buider = PDF_Buider(file_out)
doc = obj_PDF_Buider.multiBuild(Story)
"""
