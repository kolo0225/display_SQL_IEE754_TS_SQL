# text_in_to_list.py

# Purpose:
#   it turns a file.txt in to list

class FileInListConverter:
    
    def __init__(self,file_text):
        self.file_text  = file_text

    def file_in_list_converter(self):

        list_1d = []
        with open(self.file_text, 'r') as r:
            list_1d = r.read().splitlines()             

        #print(list_1d)

        return list_1d

