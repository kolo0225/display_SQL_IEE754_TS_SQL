# build_pdf_v4.py

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

# import modules:
from header_n_footer_v1 import combine_header_footer  # uncommented

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

