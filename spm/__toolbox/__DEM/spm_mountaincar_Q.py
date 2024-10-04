from spm.__wrap__ import _Runtime


def spm_mountaincar_Q(*args, **kwargs):
  """  Desired ensemble density  
    FORMAT [Q] = spm_mountaincar_Q(x)  
     
    x:  (n x m) matrix of n m-D point in states space  
     
    Q   - desired equilibrium density; p(x)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_mountaincar_Q.m)
  """

  return _Runtime.call("spm_mountaincar_Q", *args, **kwargs)
