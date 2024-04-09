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
    

'''
# holodeck from Chen 2019
class GSMF_Schechter(_Galaxy_Stellar_Mass_Function):
    r"""Single Schechter Function - Galaxy Stellar Mass Function.

    This is density per unit log10-interval of stellar mass, i.e. $\Phi = dn / d\log_{10}(M)$

    See: [Chen2019]_ Eq.9 and enclosing section.

    """

    def __init__(self, phi0=-2.77, phiz=-0.27, mchar0_log10=11.24, mchar0=None, mcharz=0.0, alpha0=-1.24, alphaz=-0.03):
        mchar0, _ = utils._parse_val_log10_val_pars(
            mchar0, mchar0_log10, val_units=MSOL, name='mchar0', only_one=True
        )

        self._phi0 = phi0         # - 2.77  +/- [-0.29, +0.27]  [log10(1/Mpc^3)]
        self._phiz = phiz         # - 0.27  +/- [-0.21, +0.23]  [log10(1/Mpc^3)]
        self._mchar0 = mchar0       # 10^ (+11.24  +/- [-0.17, +0.20]  [log10(Msol)])
        self._mcharz = mcharz       #  0.0                        [log10(Msol)]    # noqa
        self._alpha0 = alpha0     # -1.24   +/- [-0.16, +0.16]
        self._alphaz = alphaz     # -0.03   +/- [-0.14, +0.16]
        return

    def __call__(self, mstar, redz):
        r"""Return the number-density of galaxies at a given stellar mass.

        See: [Chen2019]_ Eq.8

        Parameters
        ----------
        mstar : scalar or ndarray
            Galaxy stellar-mass in units of [grams]
        redz : scalar or ndarray
            Redshift.

        Returns
        -------
        rv : scalar or ndarray
            Number-density of galaxies per log-interval of mass in units of [Mpc^-3]
            i.e.  ``Phi = dn / d\\log_{10}(M)``

        """
        phi = self._phi_func(redz)
        mchar = self._mchar_func(redz)
        alpha = self._alpha_func(redz)
        xx = mstar / mchar
        # [Chen2019]_ Eq.8
        rv = np.log(10.0) * phi * np.power(xx, 1.0 + alpha) * np.exp(-xx)
        return rv

    def _phi_func(self, redz):
        """See: [Chen2019]_ Eq.9
        """
        return np.power(10.0, self._phi0 + self._phiz * redz)

    def _mchar_func(self, redz):
        """See: [Chen2019]_ Eq.10 - NOTE: added `redz` term
        """
        return self._mchar0 + self._mcharz * redz

    def _alpha_func(self, redz):
        """See: [Chen2019]_ Eq.11
        """
        return self._alpha0 + self._alphaz * redz
'''