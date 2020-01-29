def this_leibniz_term(term_index):
    return (4.0/(term_index*2+1))*((-1)**(term_index))  
    
def leibniz_sum(number_of_terms):
    term_generator = (this_leibniz_term(x) for x in range(number_of_terms))
    
    return sum(term_generator)

def arctan_z_term(z, term_index):
    return (z/(term_index*2+1))*((-1)**(term_index))      
    
   