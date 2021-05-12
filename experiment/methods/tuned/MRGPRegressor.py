from ..MRGPRegressor import complexity, model
from ..src.mrgp import MRGPRegressor
from .params._mrgpregressor import params

est=MRGPRegressor(max_len=6,
                  )

est.set_params(**params)

# double the evals
est.time_out=8*60*60
est.g = int(est.g*2**0.5)
est.popsize = int(est.popsize*2**0.5)
