from spm.__wrap__ import _Runtime


def spm_multrnd(*args, **kwargs):
  """  Sample from multinomial distribution  
    FORMAT [m] = spm_multrnd(p,N)  
     
    p    - [M x 1] vector of probabilities  
    N    - Number of samples to generate  
      
    m    - [N x 1] vector of samples, where each sample is number from 1 to M  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_multrnd.m)
  """

  return _Runtime.call("spm_multrnd", *args, **kwargs)
