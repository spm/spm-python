from spm.__wrapper__ import Runtime


def spm_barh(*args, **kwargs):
  """  Density plotting function (c.f. bar - horizontal)  
    FORMAT spm_barh(E,C,[P])  
    E   - (n x 1) expectation  
    C   - (n x 1) variances  
    P   - (n x 1) priors  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_barh.m)
  """

  return Runtime.call("spm_barh", *args, **kwargs, nargout=0)
