import numpy as np

class GSMF_Base:
    def __call__(self, *args, **kwargs):
        raise NotImplementedError("Subclasses must implement __call__ method.")
    
class GSMF_Schechter(GSMF_Base):
    def __init__(self, phi_0=-2.77, phi_z=-0.27, log_m0=11.24, alpha_0=-1.24, alpha_z=-0.03):
        self._phi_0 = phi_0
        self._phi_z = phi_z
        self._log_m0 = log_m0
        self._alpha_0 = alpha_0
        self._alpha_z = alpha_z

    def __call__(self, mass, other_params):
        # want to restrict what specific models can take so don't use *args and **kwargs
        return "How ever you calculate this :))"
    
    def _phi_func(self, redshift):
        _log_phi = self._phi_0 + self._phi_z * redshift
        return np.power(10.0, _log_phi)
    
    #### continue writing these functions
    #### remember to use _variable to define private functions and variables