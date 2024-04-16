from astropy.cosmology import WMAP9 as cosmo
import astropy.units as u

class Cosmology:
    def __init__(self):
        self._h_0 = cosmo.H(0)  #.to(u.) convert to units here or later?

    def _hz_func(self, redshift):
        Hz = cosmo.H(redshift) #.to(u.) convert units here or not?
        return Hz

    def _dt_dz_func(self, redshift):
        # dt/dz = 1/(1+z)*H(0) - H(z)

        Hz = self._hz_func(redshift)
        dt_dz = 1 / ((1 + redshift)*self._h_0 - Hz)
        return dt_dz


