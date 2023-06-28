# DirectoriesControl.py 

# purpose:
#   create directories with the timestamp attached to the directory name
#   move files in to this directory
#   zip directory when is over
#   auto-opens selected documents 

# Packages:
import os
import shutil
from datetime import datetime

# ===========================================================================
class DirectoryFileManager:
    
    def __init__ (self, dir_name, list_tobe_copied, list_tobe_invoked):
        
        self.dir_name          = dir_name
        self.list_tobe_copied  = list_tobe_copied
        self.list_tobe_invoked = list_tobe_invoked
        
    def zip_directory(self):  
        
        dir_full_path =self.copy_files_to_directory()
        shutil.make_archive(dir_full_path, 'zip', dir_full_path)
        
        return
    def invoke_files_selected(self):
        
        for file in self.list_tobe_invoked:
            os.system("start "+file)
        
        return
        
    def copy_files_to_directory(self):  
        
        dir_full_path = self.create_directory()
        
        for file in self.list_tobe_copied:
            shutil.copy(file,dir_full_path)
        
        return dir_full_path

    def create_directory(self):
        
        # Date time
        current_date = datetime.now()
        date_str     = current_date.strftime('%m_%d_%y__%H_%M')
        # use DateTime to create directory
        current_dir         = os.getcwd()
        directory_name = self.dir_name + date_str
        dir_full_path  = current_dir+directory_name
        #print(dir_full_path)
        
        os.mkdir(dir_full_path)
        #print("directory is ready")
        
        return dir_full_path
