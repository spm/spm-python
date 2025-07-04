from spm._runtime import Runtime


def spm_mesh_curvature(*args, **kwargs):
    """
      Compute a crude approximation of the curvature of a surface mesh  
        FORMAT C = spm_mesh_curvature(M)  
        M        - a patch structure  
         
        C        - curvature vector  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mesh_curvature.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mesh_curvature", *args, **kwargs)
