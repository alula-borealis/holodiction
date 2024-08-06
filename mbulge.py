import numpy as np
import constant as const

class MbulgeBase:
    def __call__(self, *args, **kwargs):
        raise NotImplementedError("Subclasses must implement __call__ method.")

class MbulgeRelation(MbulgeBase):
    def __init__(self, m_star=10**8.17, alpha_star=1.01, epsilon=0.4, ref_m=10**11):
        # see written python notes (9) for a different way to define default values
        # need to decide whether I want to change these dyanmically between instances
        self._m_star = m_star
        self._alpha_star = alpha_star
        self._epsilon = epsilon
        self._ref_m = ref_m

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
        
    def _scaling_func(self, m_bulge):
        # see second eqn on Mbulge relation
        # use np.random.lognormal?
        _mean = self._m_star * (m_bulge / self._ref_m)**self._alpha_star
        _standard_d = self._epsilon
        #_distribution = np.random.lognormal or scipy?
        # scipy.stats.lognorm doesn't seem to import but scipy does, issue between pip and conda?

    ### !! Need to add __call__