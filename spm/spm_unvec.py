from spm.__wrap__ import _Runtime


def spm_unvec(*args, **kwargs):
  """  Unvectorise a vectorised array - a compiled routine  
    FORMAT [varargout] = spm_unvec(vX,varargin)  
    varargin  - numeric, cell or structure array  
    vX        - spm_vec(X)  
     
    i.e. X           = spm_unvec(spm_vec(X),X)  
         [X1,X2,...] = spm_unvec(spm_vec(X1,X2,...),X1,X2,...)  
     
    See spm_vec  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_unvec.m)
  """

  return _Runtime.call("spm_unvec", *args, **kwargs)
