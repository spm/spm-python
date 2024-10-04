from spm.__wrap__ import _Runtime


def bf_inverse_eloreta(*args, **kwargs):
  """  Computes eLORETA projectors  
     
    please cite  
    R.D. Pascual-Marqui: Discrete, 3D distributed, linear imaging methods of electric neuronal activity. Part 1: exact, zero  
    error localization. arXiv:0710.3341 [math-ph], 2007-October-17, http://arxiv.org/pdf/0710.3341  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_inverse_eloreta.m)
  """

  return _Runtime.call("bf_inverse_eloreta", *args, **kwargs)
