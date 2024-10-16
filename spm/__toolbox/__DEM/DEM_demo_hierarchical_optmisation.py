from spm.__wrapper__ import Runtime


def DEM_demo_hierarchical_optmisation(*args, **kwargs):
  """  This is the same as spm_nlsi_GH but tries to model the free energy as a  
    function of conditional expectations using a sparse mixture of scaled  
    Gaussians. The objective is to account for local maxima when optimising  
    free energy by recasting the problem in terms of a parameterised mapping   
    from conditional expectation to free energy explicitly.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_hierarchical_optmisation.m)
  """

  return Runtime.call("DEM_demo_hierarchical_optmisation", *args, **kwargs, nargout=0)
