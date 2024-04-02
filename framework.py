import constants

# create a class which defines the parameter space
# will have 3/4 arguments - z, m, q, f

# holodecks grid
"""# ---- Create SAM grid edges

        if shape is not None:
            if np.isscalar(shape):
                shape = [shape for ii in range(3)]

        params = [mtot, mrat, redz]
        param_names = ['mtot', 'mrat', 'redz']
        for ii, (par, name) in enumerate(zip(params, param_names)):
            if not isinstance(par, tuple) and (len(par) == 3):
                err = (
                    f"{name} (type={type(par)}, len={len(par)}) must be a (3,) tuple specifying a log-spacing, "
                    "or ndarray of grid edges!"
                )
                log.exception(err)
                raise ValueError(err)

            par = [pp for pp in par]
            if shape is not None:
                if shape[ii] is not None:
                    par[2] = shape[ii]
            params[ii] = np.logspace(*np.log10(par[:2]), par[2]+1)
            log.debug(f"{name}: [{params[ii][0]}, {params[ii][-1]}] {params[ii].size}")

        mtot, mrat, redz = params
        self.mtot = mtot
        self.mrat = mrat
        self.redz = redz
"""
# and they then specify the shape sam = sam.Semi_Analytic_Model(shape=30)

class ParameterGrid:
    def __init__(self, mtot, mrat, redz, shape=None):
        self.mtot = mtot
        self.mrat = mrat
        self.redz = redz
        self.shape = shape

    def create_grid(self):
        params = [self.mtot, self.mrat, self.redz]
        param_names = ['mtot', 'mrat', 'redz']
        grids = []

        for par, name in zip(params, param_names):
            par = list(par)
            if self.shape is not None:
                if self.shape[param_names.index(name)] is not None:
                    par[2] = self.shape[param_names.index(name)]
            grid = np.logspace(*np.log10(par[:2]), par[2] + 1)
            grids.append(grid)
            print(f"{name}: [{grid[0]}, {grid[-1]}] {grid.size}")

        return grids

# Example usage:
mtot = (1, 100, 10)  # Log-spaced between 1 and 100, with 10 points
mrat = (0.1, 0.9, 5)  # Log-spaced between 0.1 and 0.9, with 5 points
redz = (0, 2, 8)  # Log-spaced between 0 and 2, with 8 points
shape = [None, None, None]  # Shape of the parameter space, None for automatic calculation

param_grid = ParameterGrid(mtot, mrat, redz, shape)
grids = param_grid.create_grid()