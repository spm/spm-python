from spm.__wrap__ import _Runtime


def nanvar(*args, **kwargs):
  """  FORMAT: Y = NANVAR(X,FLAG,DIM)  
      
       This file is intended as a drop-in replacement for Matlab's nanvar. It  
       originally forms part of the NaN suite:  
       http://www.mathworks.com/matlabcentral/fileexchange/6837-nan-suite/  
       and was modified to be compatible.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/external/stats/nanvar.m)
  """

  return _Runtime.call("nanvar", *args, **kwargs)
