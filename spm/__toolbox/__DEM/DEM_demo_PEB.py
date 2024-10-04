from spm.__wrap__ import _Runtime


def DEM_demo_PEB(*args, **kwargs):
  """  DEM demo for a hierarchical linear model (MFX).  This inversion is  
    cross-validated with restricted maximum likelihood using and parametric  
    empirical Bayes (spm_PEB). It uses a simple two level model that embodies  
    empirical shrinkage priors on the first-level parameters (c.f.,  
    DEM_demo_GLM, with no empirical priors)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_PEB.m)
  """

  return _Runtime.call("DEM_demo_PEB", *args, **kwargs, nargout=0)
