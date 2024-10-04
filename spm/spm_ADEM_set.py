from spm.__wrap__ import _Runtime


def spm_ADEM_set(*args, **kwargs):
  """  Perform checks on DEM structures for active inversion  
    FORMAT DEM = spm_ADEM_set(DEM)  
     
    DEM.G  - generative model  
    DEM.M  - recognition model  
    DEM.C  - exogenous causes  
    DEM.U  - prior expectation of causes  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_ADEM_set.m)
  """

  return _Runtime.call("spm_ADEM_set", *args, **kwargs)
