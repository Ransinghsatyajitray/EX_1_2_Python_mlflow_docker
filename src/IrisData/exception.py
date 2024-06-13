# We will create custom exception class, debug


# utils.py is a helper module
# saving the model, loading the model, reading the data from any where, 

import sys

class customexception(Exception):
    def __init__(self, error_message, error_details):
        self.error_message = error_message
        _,_,exc_tb = error_details.exec_info()
        
        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        
    def __str__(self):
        return f"Error occured in python script name [{self.file_name}] line number [{self.lineno}] error message [{self.error_message}]"
    
    
    
    if __name__ == "__main__":
        