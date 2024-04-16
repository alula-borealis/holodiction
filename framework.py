# libraries
import numpy as np
import matplotlib.pyplot as plt

# user-defined modules
import constant as const
import gsmf
import gpf
import gmt
import mbulge

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
'''
class ParameterGrid:
    def __init__(self, mtot, mrat, redz, shape=None):
        self.masstot = mtot
        self.mrat = mrat
        self.redz = redz
        self.shape = shape

    def create_grid(self):
        params = [mtot, mrat, redz]
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


mtot = (1, 100, 10)  # Log-spaced between 1 and 100, with 10 points
mrat = (0.1, 0.9, 5)  # Log-spaced between 0.1 and 0.9, with 5 points
redz = (0, 2, 8)  # Log-spaced between 0 and 2, with 8 points
shape = [None, None, None] 

param_grid = ParameterGrid(mtot, mrat, redz, shape)
grids = param_grid.create_grid()
print(grids)
'''

## Might be better to not define a rigid grid and instead handle parameters dynamically
## so we can change the resolution in different parts more easily
## holodeck produces a fixed grid like this 

class ParameterSpace:
    # the __init__ function is always executed when the class is initiated
    # self individualises an object, so each name generated is it's own
    def __init__(self, mass, mass_ratio, redshift, size):
        self.mass = mass
        self.mass_ratio = mass_ratio
        self.redshift = redshift
        self.size = size

    # * unpacks the elements of the iterables as separate arguments
    # so if mass = (1, 10), it unpacks them into 1 and 10 and gives them to np.logspace as arguments
    # num = number of samples to generate
    def generate_grid(self):
        mass_params = np.logspace(*self.mass, num = self.size[0])
        mass_ratio_params = np.logspace(*self.mass_ratio, num = self.size[1])
        redshift_params = np.logspace(*self.redshift, num = self.size[2])

        print("mass: ", mass_params)
        print('mass ratio: ', mass_ratio_params)
        print('redshift: ', redshift_params)

        self.m, self.q, self.z = np.meshgrid(mass_params, mass_ratio_params, redshift_params, indexing='xy')

    def get_grid(self):
        # checks if grid has been generated (hasattr) and generates it if it hasn't (self.generate_grid())
        if not hasattr(self, 'm'):
            self.generate_grid()
        # returns the grid stored in the grid attribute of the instance
        return self.m, self.q, self.z
    
# Example usage:
mass_range = np.log10((1e6, 1e9))  # Define the range for mass 
mass_ratio_range = np.log10((0.1, 1))  # Define the range for mass ratio 
redshift_range = np.log10((1, 5))  # Define the range for redshift 
grid_shape = (5, 5, 5)  # Define the shape of the grid

# Instantiate the ParameterGrid class
param_grid = ParameterSpace(mass_range, mass_ratio_range, redshift_range, grid_shape)

# Get the grid
m_grid, q_grid, z_grid = param_grid.get_grid()

print("m grid: ", m_grid)
print("q grid: ", q_grid)
print("z grid: ", z_grid)
'''
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.scatter(m_grid, q_grid, z_grid)

ax.set_xlabel("mass")
ax.set_ylabel("mass ratio")
ax.set_zlabel("redshift")

plt.show()
'''
## do the numbers in each array make sense?
## not super sure meshgrid is the right thing to use
# matrix or cartesian?
# do I implement frequency?


