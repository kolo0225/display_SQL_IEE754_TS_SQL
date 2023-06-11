# html_splitter_N_pdf_maker.py

# it split html based on page
# takes a screenshot of the html

# Note:
#   image has watermarks on due to 
#   aspose is a paid library
# --------------------------

from html2image import Html2Image
import aspose.words as aw

doc = aw.Document("PRealRampRataIncrDecrTest.html")
hti = Html2Image()
css = "body {background: white;}"
 
for page in range(0, doc.page_count):
    extractedPage = doc.extract_pages(page, 1)
    extractedPage.save(f'temp_Output_{page + 1}.html')

html_list = ['temp_Output_1.html','temp_Output_2.html','temp_Output_3.html']
for index,file in enumerate(html_list):
    hti.screenshot(
        html_file=file, css_str=css, save_as=f'temp_sreenshot_{index}.png'
    )

# Splits the html file & Creates png
## it shows with watermarks (not good)
# --------------------------
def html_splitterNconverter_to_png (self, file):
        
    # adjusts name
    core_name = file.replace('.html','')
    png_name  = core_name + '.png'
       
    doc = aw.Document(file)
            
    for page in range(0, doc.page_count):
        extractedPage = doc.extract_pages(page, 1)
        #extractedPage.save(f"temp_Output_{page + 1}.html")
            
        hti = Html2Image()
        hti.screenshot(
        html_file=extractedPage, save_as=png_name
        )
                    
    return png_name