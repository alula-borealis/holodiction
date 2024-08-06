"""Constants"""

import numpy as np
import astropy as ap
import astropy.constants
import astropy.units

# all SI units
PI = np.pi
YR = ap.units.year.to(ap.units.s)   # convert year to seconds
MSOL = ap.constants.M_sun.value     # mass of sun
PC = ap.constants.pc.value          # parsec
MPC = 1.0e6*PC               # mega-parsec
NG = ap.constants.G.value           # Newton's G
LC = ap.constants.c.value           # speed of light

