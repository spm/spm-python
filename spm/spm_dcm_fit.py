from spm.__wrap__ import _Runtime


def spm_dcm_fit(*args, **kwargs):
  """  Bayesian inversion of DCMs using Variational Laplace  
    FORMAT [DCM] = spm_dcm_fit(P)  
     
    P          - {N x M} DCM structure array (or filenames) from N subjects  
    use_parfor - if true, will attempt to run in parallel (default: false)  
                 NB: all DCMs are loaded into memory  
     
    DCM  - Inverted (1st level) DCM structures with posterior densities  
   __________________________________________________________________________  
     
    This routine is just a wrapper that calls the appropriate dcm inversion  
    routine for a set a pre-specifed DCMs.  
     
    If called with a cell array, each column is assumed to contain 1st level  
    DCMs inverted under the same model. Each row contains a different data  
    set (or subject).  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_dcm_fit.m)
  """

  return _Runtime.call("spm_dcm_fit", *args, **kwargs)
