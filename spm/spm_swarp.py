from spm.__wrapper__ import Runtime


def spm_swarp(*args, **kwargs):
  """  Warp surface  
    FORMAT that = spm_swarp(this,def)  
    this - a gifti object  
    def  - a deformation (nifti object or filename)  
    that - the warped gifti object  
     
    FORMAT that = spm_swarp(this,def,M)  
    this - a gifti object  
    def  - a deformation field (nx*ny*nz*1*3)  
    M    - mapping from voxels to world, for deformation field  
    that - the warped gifti object  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_swarp.m)
  """

  return Runtime.call("spm_swarp", *args, **kwargs)
