from spm.__wrap__ import _Runtime


def spm_get_data(*args, **kwargs):
  """  Get data from image files at specified locations  
    FORMAT [Y] = spm_get_data(V,XYZ,check)  
     
    V          - [1 x n] struct array of file handles (or filename matrix)  
    XYZ        - [3 x m] or [4 x m] location matrix {voxel}  
    check      - check validity of input parameters [default: true]  
     
    Y          - [n x m] double values  
     
    See also spm_sample_vol  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_get_data.m)
  """

  return _Runtime.call("spm_get_data", *args, **kwargs)
