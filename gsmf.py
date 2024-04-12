import numpy as np

# do I need to make the base classes private?
class GSMF_Base:
    def __call__(self, *args, **kwargs):
        raise NotImplementedError("Subclasses must implement __call__ method.")
    
class GSMF_Schechter(GSMF_Base):
    # see equations 8-11 in [Chen 2019]
    def __init__(self, phi_0=-2.77, phi_z=-0.27, log_m0=11.24, alpha_0=-1.24, alpha_z=-0.03):
        self._phi_0 = phi_0
        self._phi_z = phi_z
        self._log_m0 = log_m0
        self._alpha_0 = alpha_0
        self._alpha_z = alpha_z

    def _phi_func(self, redshift):
        _log_phi = self._phi_0 + self._phi_z * redshift
        return np.power(10.0, _log_phi)
    
    def _scale_m_func(self):
        # holodeck has this function as M_0 + M_z * z but with M_z = 0.0
        return np.power(10.0, self._log_m0)
    
    def _alpha_func(self, redshift):
        return self._alpha_0 + self._alpha_z * redshift

    def __call__(self, stellar_mass, redshift):
        # want to restrict what specific models can take so don't use *args and **kwargs
        # __call__ allows class to be called as a function
        phi = self._phi_func(redshift)
        scale_mass = self._scale_m_func()
        alpha = self._alpha_func(redshift)

        mass_ratio = stellar_mass / scale_mass
        alpha_power = 1.0 + alpha
        
        schechter = np.log(10.0) * phi * np.power(mass_ratio, alpha_power) * np.exp(-mass_ratio)

        return schechter
    
    #### remember to use _variable to define private functions and variables