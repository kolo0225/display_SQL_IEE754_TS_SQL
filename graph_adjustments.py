# graph_adjustments.py

# Purpose:
#   To Adjust lists in order to produse desirable graphs:
#       by str -> float of selected decimal places
#       by reducing the x-axis entries for visibility

#   str_to_float_round  
#       turns string lists
#       in to mix (float/string) list 
#       and rounds
#       for the purpose of matplotlib plots
"""
# graph adjusters
list_in   = range(0,101)  # example using range from 0:101
round_num = 2
divisor   = 10
"""

class GraphAdjustments:
    
    def __init__ (self, in_list, round_num, divisor):
        
        self.in_list   = in_list
        self.round_num = round_num
        self.divisor   = divisor
        
    def reduce_list_len(self):
       
        reduced_list = []
        for index,item in enumerate(self.in_list):
            if index % self.divisor == 0:
                reduced_list.append(item)
                
        return reduced_list
        
        
    def str_to_float_round(self):
        
        float_round_list = []
        for item_str in self.in_list:
            if item_str != 'nan':
                item_float= float(item_str)
                round_item = round(item_float,self.round_num)
                float_round_list.append(round_item)
            else:
                float_round_list.append(float(item_str))
                    
        return float_round_list
        
"""
obj_GraphAdjustments = GraphAdjustments(list_in, round_num, divisor)
x_list    = obj_GraphAdjustments.less_by_fuctor_x_dispaly()
"""