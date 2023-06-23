# header_n_footer_v1.py 

# Purpose:
#   To create the headers & footers 
#   of the pdf 
#   similar to the companies stile
#   it also provides the numbering of the pages


# ==========================================================
# header packages:
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm, inch
from reportlab.lib.colors import red, orange, orangered,  green, darkcyan, blue, darkblue, darkslateblue, darkslategray, black
from reportlab.platypus import PageBreak
from reportlab.platypus.paragraph import Paragraph


def header_also(canvas, doc):
    
    header_also = PS(name = 'header_big1',
                fontSize = 20,
                leading  = 30,
                fontName = 'Times',
                alignment= TA_RIGHT,
                textColor= darkcyan)
        
    header_also =  Paragraph('Tasos' , header_also)
    
    canvas.saveState()
    w, h = header_also.wrap(doc.width, doc.topMargin)
    header_also.drawOn(canvas, doc.leftMargin, doc.height + doc.bottomMargin + doc.topMargin - h)
    canvas.restoreState()
    
def header_stem(canvas, doc):
    
    header_stem = PS(name = 'header_small',
                fontSize = 8,
                leading  = 16,
                fontName = 'Times',
                alignment= TA_RIGHT,
                textColor= black)
        
    header_stem =  Paragraph('a python coder' , header_stem)
    
    canvas.saveState()
    w, h = header_stem.wrap(doc.width, doc.topMargin)
    header_stem.drawOn(canvas, doc.leftMargin+ 0.75*inch, doc.height + doc.bottomMargin + doc.topMargin - h- 0.2*inch)
    canvas.restoreState()
    
def header_energy(canvas, doc):
    
    header_energy = PS(name = 'header_big2',
                fontSize = 20,
                leading  = 30,
                fontName = 'Times',
                alignment= TA_RIGHT,
                textColor= darkslategray)
        
    header_energy =  Paragraph('Kolovos' , header_energy)
    
    canvas.saveState()
    w, h = header_energy.wrap(doc.width, doc.topMargin)
    header_energy.drawOn(canvas, doc.leftMargin+ 0.45*inch, doc.height + doc.bottomMargin + doc.topMargin - h- 0.25*inch)
    canvas.restoreState()
    
def footer_black(canvas, doc):
    
    footer_black = PS(name = 'footer_dark',
                fontSize = 8,
                leading  = 16,
                fontName = 'Times',
                alignment= TA_LEFT,
                textColor= darkslategray)
        
    footer_black =  Paragraph('https://github.com/kolo0225   |   USA   |   https://www.linkedin.com/in/anastasios-tasos-kolovos-0585b994/', footer_black)
    
    canvas.saveState()
    w, h = footer_black.wrap(doc.width, doc.bottomMargin)
    footer_black.drawOn(canvas, doc.leftMargin, h)
    canvas.restoreState()
    
def footer_orange(canvas, doc):
    
    footer_orange = PS(name = 'footer_light',
                fontSize = 8,
                leading  = 16,
                fontName = 'Times',
                alignment= TA_CENTER,
                textColor= orangered)
        
    footer_orange =  Paragraph('stay happy and motivated', footer_orange)
    
    canvas.saveState()
    w, h = footer_orange.wrap(doc.width, doc.bottomMargin)
    footer_orange.drawOn(canvas, doc.leftMargin, h+ 0.25*inch)
    canvas.restoreState()

def footer_paging(canvas, doc):
    
    footer_paging = PS(name = 'footer_page',
                fontSize = 8,
                leading  = 16,
                fontName = 'Times',
                alignment= TA_RIGHT,
                textColor= black)
        
    canvas.saveState()
    page_num = canvas.getPageNumber()
    page_num = str(page_num)
    footer_paging =  Paragraph( page_num , footer_paging)
    w, h = footer_paging.wrap(doc.width, doc.bottomMargin)
    footer_paging.drawOn(canvas, doc.leftMargin+ 0.25*inch, h)
    canvas.restoreState()

def combine_header_footer(canvas, doc):
    header_also(canvas, doc)
    header_stem(canvas, doc)
    header_energy(canvas, doc)
    footer_black(canvas, doc)
    footer_orange(canvas, doc)
    footer_paging(canvas, doc)
    
