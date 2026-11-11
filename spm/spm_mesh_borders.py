from spm._runtime import Runtime


def spm_mesh_borders(*args, **kwargs):
    r"""
      Return borders of a triangle mesh  
        FORMAT [B,C] = spm_mesh_borders(M)  
        M            - a [nx3] faces array or a patch handle/structure  
         
        B            - a [mx1] vector of indices of border vertices  
        C            - a cell array of indices of contiguous border vertices  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_mesh_borders.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mesh_borders", *args, **kwargs)
