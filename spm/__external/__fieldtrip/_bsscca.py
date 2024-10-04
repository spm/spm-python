from spm.__wrap__ import _Runtime


def _bsscca(*args, **kwargs):
  """  BSSCCA computes the unmixing matrix based on the canonical correlation between   
    two sets of (possibly multivariate) signals, the sets may contain time shifted copies.   
    In its default, it implements the algorithm described in [1], computing the  
    canonical correlation between a set of signals and their lag-one-shifted  
    copy. Alternatively, if the input contains a reference signal (possibly multivariate),  
    the canonical correlation between the data in X and the reference signal is computed.  
    It requires JM's cellfunction toolbox on the MATLAB path:  
     (github.com/schoffelen/cellfunction.git)  
     
    [1] DeClercq et al 2006, IEEE Biomed Eng 2583.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/bsscca.m)
  """

  return _Runtime.call("bsscca", *args, **kwargs)
