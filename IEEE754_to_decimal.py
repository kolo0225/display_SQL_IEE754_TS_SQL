# IEEE754_to_decimal.py

# Purpose:
#       converts IEEE754 numbers in to decimal


# variable
#num_d_ieee = [1092616192,1101004800,1106247680,1109393408,1112014848]

class IEEE754toDecimal:

    def __init__(self, num_d_ieee):
   
        num_b_ieee = bin(num_d_ieee)
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
        
        for p, exp in enumerate(mantissa_list):
  
            if (exp == "1"):
                mantissa += 2**(-1-p)
       
        #print(mantissa) 
        return mantissa
        
        
    def fn_exponent(self):
        
        exponent_list = self.num_b_ieee[2:10]
        expnt      = 0
        
        for p, exp in enumerate(exponent_list):
  
            if (exp == "1"):
    
                expnt += 2**(7-p)
        
        
        expnt    =  expnt-127
        exponent = 2**expnt
        
        #print(exponent)
        return exponent
      
    def fn_sign(self):
        
        sign_bit   = self.num_b_ieee[0]
        
        if sign_bit == "0":
            sign =  1
        else:
            sign = -1
            
        #print(sign)
        return sign

#obj_IEEE754toDecimal    = IEEE754toDecimal(num_d_ieee)
#obj_IEEE754toDecimal.fn_sign()
#obj_IEEE754toDecimal.fn_exponent()
#obj_IEEE754toDecimal.fn_mantissa()
#obj_IEEE754toDecimal.fn_main()

"""
for index in range(len(num_d_ieee)):

    obj_IEEE754toDecimal    = IEEE754toDecimal(num_d_ieee[index])
    obj_IEEE754toDecimal.fn_main()
"""