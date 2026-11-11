from spm._runtime import Runtime


def spm_mesh_curvature(*args, **kwargs):
    r"""
      Compute a crude approximation of the curvature of a surface mesh  
        FORMAT C = spm_mesh_curvature(M)  
        M        - a patch structure  
         
        C        - curvature vector  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_mesh_curvature.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mesh_curvature", *args, **kwargs)
