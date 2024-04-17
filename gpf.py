import numpy as np
import constant as const

class GPFBase:
    def __call__(self, *args, **kwargs):
        raise NotImplementedError("Subclasses must implement __call__ method.")
    
class GPFPowerLaw(GPFBase):
    def __init__(self, alpha_f=0.0, beta_f=0.8, gamma_f=0.0, f0=0.025, q_max=1.0, q_min=0.25, ref_m=10e11):
        # see equation 12 and 14 from [Chen 2019] - think they use this one in holodeck
        # holodeck have q_max=1.0 and q_min=0.25 but can't find in literature - Mundy et al??
        self._alpha_f = alpha_f
        self._beta_f = beta_f
        self._gamma_f = gamma_f
        self._f0 = f0
        self._q_max = q_max
        self._q_min = q_min
        self._ref_m = ref_m

    def _f0_prime_func(self):
        # this is eqn. 15 of [Chen 2019] after integrating over the mass ratio
        pow = 1.0 + self._gamma_f
        q_norm = (np.power(self._q_max, pow) - np.power(self._q_min, pow)) / (pow)

        return self._f0 / q_norm

    def __call__(self, galaxy_mass, mass_ratio, redshift):
        f0_prime = self._f0_prime_func()
        norm_mass = galaxy_mass / self._ref_m
        af = self._alpha_f
        bf = self._beta_f
        gf = self._gamma_f

        # holodeck also add in a max fraction (between 0 and 1) - might want to add later

        diff_pair_frac = f0_prime * np.power(norm_mass, af) * np.power((1.0 + redshift), bf) * np.power(mass_ratio, gf)

        return diff_pair_frac




