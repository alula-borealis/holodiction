import numpy as np
import constant as const

class Mbulge_Base:
    def __call__(self, *args, **kwargs):
        raise NotImplementedError("Subclasses must implement __call__ method.")

class Mbulge_Relation(Mbulge_Base):
    def __init__(self, m_star=10**8.17, alpha_star=1.01, epsilon=0.4):
        self._m_star = m_star
        self._alpha_star = alpha_star
        self._epsilon = epsilon

    # phenomenological fitting function to link bulge mass to stellar mass
    def _mstar_to_mbulge(self, mass):
        _bulge_frac_low = 0.615
        _denom = (np.log10(mass) - 10)
        _bulge_frac_high = (np.sqrt(6.9) / np.power(_denom, 1.5)) * np.exp(-3.45/_denom) + _bulge_frac_low

        if np.log10(mass) > 10.0:
            return _bulge_frac_high
        else:
            return _bulge_frac_low
        
        # these return m_bulge/m
        
    def _scaling_func(self):
        # see second eqn on Mbulge relation
        # use np.random.lognormal?