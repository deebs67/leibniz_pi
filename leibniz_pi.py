# This importable Python file implements functions for calculating Pi using the Gregory-Leibniz series. See associated README.md file
# for more information.
#
# (c) deebs67, 2020 (MIT licensed)
#
import math


def this_leibniz_term(term_index):
    """
    Calculates a single term in the version of the Gregory-Leibniz series for calculating Pi from Pi/4.
    Note that this particular method is conceptually very simple, but converges very slowly.
    See README.md for more discussion.
    
    """
    return (4.0/(term_index*2+1))*((-1)**(term_index))  
    

def leibniz_sum(number_of_terms):
    """
    Sume over the individual terms in the Gregory-Leibniz series for calculating Pi from Pi/4.
    Note that this particular method is conceptually very simple, but converges very slowly.
    See README.md for more discussion.
    
    """
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
   