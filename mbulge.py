import numpy as np
import constant as const

class Mbulge_Base:
    def __call__(self, *args, **kwargs):
        raise NotImplementedError("Subclasses must implement __call__ method.")

class Mbulge_Relation(Mbulge_Base):
    def __init__(self, parameters):
        self._parameters = parameters

    def _mstar_to_mbulge_(self, mass):
        if np.log10(mass) > 10.0:
            return np.sqrt(6.9) # see mbulge relation notes to finish this