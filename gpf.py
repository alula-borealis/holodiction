import numpy as np

class GPF_Base:
    def __call__(self, *args, **kwargs):
        raise NotImplementedError("Subclasses must implement __call__ method.")
    
class GPF_Power_Law(GPF_Base):
    def __init__(self, default_parameters):
        # see equation 12 from [Chen 2019] - think they use this one in holodeck
        self._default_parameters = default_parameters