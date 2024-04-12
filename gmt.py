import numpy as np
import constant as const

class GMT_Base:
    def __call__(self, *args, **kwargs):
        raise NotImplementedError("Subclasses must implement __call__ method.")
    
class GMT_Power_Law(GMT_Base):
    def __init__(self, tau_0=1.05, alpha_tau=0.0, beta_tau=-0.5, gamma_tau=0.0, ref_m=10e11, h0=0.7):
        self._tau_0 = tau_0
        self._alpha_tau = alpha_tau
        self._beta_tau = beta_tau
        self._gamma_tau = gamma_tau
        self._ref_m = ref_m
        self._h0 = h0

    def __call__(self, galaxy_mass, mass_ratio, redshift):
        ref_mb = (0.4 / self._h0) * (self._ref_m)
        norm_mass_b = galaxy_mass / ref_mb

        tau = self._tau_0
        at = self._alpha_tau
        bt = self._beta_tau
        gt = self._gamma_tau

        timescale = tau * np.power(norm_mass_b, at) * np.power(1.0 + redshift, bt) * np.power(mass_ratio, gt)
        return timescale