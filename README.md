# leibniz_pi
Python functions to approximate Pi using the Leibniz formula

For some description of the Leibniz formula for generating Pi/4, see:
https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80

But in a nutshell, Pi can be approximated as follows:

Pi = 4 - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + ...

However, the convergence is *very* slow, so you need thousands of terms to generate only a few decimal digits!

To run the code in Python3:

import leibniz_pi

leibniz_pi.leibniz_sum(1_000_000)  # For 1M terms in the above sum, say

