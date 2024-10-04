from spm.__wrap__ import _Runtime


def spm_pca_warps(*args, **kwargs):
  """ __________________________________________________________________________  
    Collection of tools for manipulating non-linear transformations (warps).  
     
    FORMAT out = warps(('warp'), in, y, (vs_in), (itrp), (bnd))  
    FORMAT y   = warps('compose', y_1, (vs_1), ..., y_n, (vs_n), (itrp))  
    FORMAT y   = warps('identity', lat_dim, (lat_vs))  
    FORMAT y   = warps('translation', T, lat_dim, (lat_vs))  
    FORMAT y   = warps('linear', L, lat_dim, (lat_vs))  
    FORMAT y   = warps('affine', A, lat_dim, (lat_vs))  
    FORMAT y   = warps('mm2vox', y, vs)  
    FORMAT y   = warps('transform', A, y)  
     
    FORMAT help warps>function  
    Returns the help file of the selected function.  
   __________________________________________________________________________  
    Copyright (C) 2017 Wellcome Trust Centre for Neuroimaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_pca_warps.m)
  """

  return _Runtime.call("spm_pac_warps", *args, **kwargs)
