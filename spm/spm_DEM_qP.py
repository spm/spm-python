from spm.__wrap__ import _Runtime


def spm_DEM_qP(*args, **kwargs):
  """  Report on conditional estimates of parameters  
    FORMAT spm_DEM_qP(qP,pP)  
     
    qP.P   - conditional expectations  
    qP.V   - conditional variance  
     
    pP     - optional priors  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_DEM_qP.m)
  """

  return _Runtime.call("spm_DEM_qP", *args, **kwargs, nargout=0)
