# images_to_pdf.py

# packages:
import os
from PIL import Image

# variables 
# ---------
out_file       = "\\results.pdf"
dir_images     = "\\SnapShot\\"

class ImageToPDFConverter:
    
    def __init__ (self, out_file, dir_images ):
        
        self.out_file   = out_file
        self.dir_images = dir_images
        
        self.dir_here       = os.getcwd()
        self.full_path      = self.dir_here + self.dir_images 
        
    def image_pdf_converter(self):
        
        list_of_images = os.listdir(self.full_path)
        
        image_list = []
        for index, item in enumerate(list_of_images):
    
            if index == 0:
                image = Image.open(self.full_path+item)
                im1 = image.convert('RGB')
                im1.save(self.dir_here + self.out_file)
            else:
                image = Image.open(self.full_path+item)
                im = image.convert('RGB')
                image_list.append(im)
                
        im1.save(self.dir_here + self.out_file, save_all=True, append_images= image_list)
            
        return 
        
obj_ImageToPDFConverter  = ImageToPDFConverter(out_file,dir_images)
obj_ImageToPDFConverter.image_pdf_converter()
    
 