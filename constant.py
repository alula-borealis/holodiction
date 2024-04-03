"""Constants"""

import numpy as np
import scipy as sp
import astropy as ap

# all SI units
#YR = ap.units.year.to(ap.units.s)   # convert year to seconds
MSOL = ap.constants.M_sun.value     # mass of sun
PC = ap.constants.pc.value          # parsec
MPC = 1.0e6*PC                      # mega-parsec
NG = ap.constants.G.value           # Newton's G
LC = ap.constants.c.value           # speed of light