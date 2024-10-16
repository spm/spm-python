from spm.__wrapper__ import Runtime


def _SAM_costfun(*args, **kwargs):
  """  costfunction for non-linear beamformer. Use this cost-function to  
    find the optimum orientation (in the tangential plane formed by  
    tanu and tanv) of the targetvoxel maximizes the pseudo_Z (i.e.  
    minimises the inverse of pseudo_Z)  
     
    positions in mm in CTF co-ordinate system  
     
    AH, 05april 2005: if origin = [], then the localspheres headmodel  
    will be used for the forward calculations. The localspheres origins  
    should be given in forward_resource (in mm in CTF co-ordinates)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/inverse/private/SAM_costfun.m)
  """

  return Runtime.call("SAM_costfun", *args, **kwargs)
