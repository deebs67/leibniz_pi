# leibniz_pi
Python functions to approximate Pi using the Gregory-Leibniz formula

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

Note that in fact the Gregory-Leibniz formula in its full form is an infinite series to calculate arctan(z), where arctan is the inverse of tan, and:

tan(theta)=Opposite/Adjacent=z

and the Gregory-Leibniz series is: theta = arctan(z) = (z^1)/1 - (z^3)/3 + (z^5)/5 - (z^7)/7 + ... ad infinitum

In 1699 the British mathematician Abraham Sharp used the Gregory-Leibniz series with z=1/sqrt(3), to compute an approximation to Pi/6, as follows:

theta=arctan(z)=Pi/6, so Pi=6*arctan(z)

In doing this, Sharp was able to calculate Pi to 71 digits, a world record at the time. So we also provide Python functions to illustrate Sharp’s method, as follows:
  
import math  
import leibniz_pi  
6.0\*leibniz_pi.arctan_z_sum(1/math.sqrt(3),1)  
3.4641016151377553  
6.0\*leibniz_pi.arctan_z_sum(1/math.sqrt(3),10)  
3.14159051093808  
6.0\*leibniz_pi.arctan_z_sum(1/math.sqrt(3),100)  
3.1415926535897936  
6.0\*leibniz_pi.arctan_z_sum(1/math.sqrt(3),1000)  
3.1415926535897936  
math.pi  
3.141592653589793  

Convergence for Sharp's approach is much more rapid than for the method shown earlier. However, Sharp’s method is conceptually slightly more complex, and does require 1/sqrt(3) to have been pre-computed to high accuracy - but he presumably would have had methods for that too!
