import math


def this_leibniz_term(term_index):
    return (4.0/(term_index*2+1))*((-1)**(term_index))  
    

def leibniz_sum(number_of_terms):
    term_generator = (this_leibniz_term(x) for x in range(number_of_terms))
    
    return sum(term_generator)


def arctan_z_term(z, term_index):
    """
    Generates each term in Gregory-Leibniz series for arctan(z)
    
    """
    term_power = (term_index*2+1)  # Each term is raised to this power, and also divided by this value
    
    return (math.pow(z, term_power)/term_power)*((-1)**(term_index))      

    
def arctan_z_sum(z, number_of_terms):
    """
    Sums over terms in Gregory-Leibniz series for arctan(z)
    
    """
    term_generator = (arctan_z_term(z, x) for x in range(number_of_terms))
    
    return sum(term_generator)
   