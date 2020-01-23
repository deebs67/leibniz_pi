# leibniz_pi
Python functions to approximate Pi using the Leibniz formula

For discussion of the meaning of Pi, and some ways (both 'analogue' and 'digital') to calculate it (including the Leibniz method), see:
https://www.mathscareers.org.uk/article/calculating-pi/

For additional discussion of the Leibniz formula for generating Pi/4, see:
https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80

However, in a nutshell, Pi can be approximated as follows:

Pi = 4 - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + ...

However, the convergence is *very* slow, so you need thousands of terms to generate only a few decimal digits! But that's not a problem if we are running Python on a modern computer. So some code has been written in file 'leibniz_pi.py'.

To run this code in Python3:

import leibniz_pi

leibniz_pi.leibniz_sum(1_000_000)  # For 1M terms in the above sum, say

