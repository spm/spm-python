from spm.__wrap__ import _Runtime


def spm_cornsweet(*args, **kwargs):
  """  generative model for psychophysical responses  
    FORMAT [y] = spm_cornsweet(P,M,U)  
    P  - model parameters  
    M  - model  
    %  
     y{1} - matched contrast level for Cornsweet effect  
     y{2} - probability of seeing Mach bands  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_cornsweet.m)
  """

  return _Runtime.call("spm_cornsweet", *args, **kwargs)
