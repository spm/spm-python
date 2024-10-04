from spm.__wrap__ import _Runtime


def DEM_demo_ALAP(*args, **kwargs):
  """  This demonstration is essentially the same as DEM_demo_LAP - however  
    here, we compare two generalised filtering schemes that are implemented  
    very differently: the first integrates the generative process in  
    parallel with the inversion, while the standard spm_LAP scheme inverts a  
    model given pre-generated data. The advantage of generating and modelling  
    data  contemporaneously is that it allows the inversion scheme to couple  
    back to the generative process through action (see active inference  
    schemes): spm_ALAP.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_ALAP.m)
  """

  return _Runtime.call("DEM_demo_ALAP", *args, **kwargs, nargout=0)
