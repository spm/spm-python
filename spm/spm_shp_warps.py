from spm.__wrapper__ import Runtime


def spm_shp_warps(*args, **kwargs):
    """
     __________________________________________________________________________  
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_shp_warps.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_shp_warps", *args, **kwargs)
