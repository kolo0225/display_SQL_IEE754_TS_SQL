# IEEE754_to_decimal.py

# Purpose:
#       converts IEEE754 numbers in to decimal

# packages:
import numpy as np

# =======================================================
class IEEE754toDecimal:

    def __init__(self, num_d_ieee):
   
        num_b_ieee = bin(num_d_ieee)
        #print(num_b_ieee)
        #print(len(num_b_ieee))
        self.num_b_ieee = num_b_ieee
        
    def fn_main(self):
    
        sign     = self.fn_sign()
        exponent = self.fn_exponent()
        mantissa = self.fn_mantissa()
        
        dec_num = sign * (1+mantissa)* exponent
        
        #print(dec_num)
        return dec_num        
        
    def fn_mantissa(self):

        mantissa_list = self.num_b_ieee[10:]
        mantissa      = 0
        
        for p, num in enumerate(mantissa_list):
  
            if (num == "1"):
                mantissa += 2**(-1-p)
       
        #print(mantissa) 
        return mantissa
        
        
    def fn_exponent(self):
        
        exponent_list = self.fn_prep_exponent()
        #exponent_list = ['1','0','0','0','1','0','0','1']
        expnt      = 0
        
        if  len(exponent_list) == 8:
            for p, exp in enumerate(exponent_list):
  
                if (exp == "1"):
    
                    expnt += 2**(7-p)
        else:
            for p, exp in enumerate(exponent_list):
  
                if (exp == "1"):
    
                    expnt += 2**(6-p)
        
        expnt    =  expnt-127
        exponent = 2**expnt
        
        #print(exponent)
        return exponent
        
        
    def fn_prep_exponent (self):
        
        len_binary       = len(self.num_b_ieee)
        
        #if len_binary == "10":
        if len_binary == 33:
            exponent_list   = self.num_b_ieee[2:10]
          
        else:
            exponent_list   = self.num_b_ieee[2:9]
         
                   
        #print(exponent_list)
        #print(len(exponent_list))
        return exponent_list

        
      
    def fn_sign(self):
        
        sign_bit   = self.num_b_ieee[0]
        
        if sign_bit == "0":
            sign =  1
        else:
            sign = -1
            
        #print(sign)
        return sign

