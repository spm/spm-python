from spm.__wrap__ import _Runtime


def spm_immune_gen(*args, **kwargs):
  """  Generative model of an immune response  
    FORMAT [Y,X] = spm_immune_gen(P,M,U)  
    Y   - timeseries data  
    X   - latent states  
    P   - Priors  
    M   - Model  
    U   - inputs (timing of measurements)  
   __________________________________________________________________________  
    Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_immune_gen.m)
  """

  return _Runtime.call("spm_immune_gen", *args, **kwargs)
