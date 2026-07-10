#   Approach 1:
import printing_functions #we are importing printing_functions.

printing_functions.print_models('raksha','001')


#   Approach 02:
from printing_functions import print_models #we are importing printing functions with different approach.

print_models('raksha','001')



#   Approach 03:
from printing_functions import print_models as pm

pm('raksha','001')



#   Approach 04:
import printing_functions as pf

pf.print_models('raksha','001')



#   Approach 05:
from printing_functions import *

print_models('raksha','001')

