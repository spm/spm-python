from spm._runtime import Runtime


def spm_mesh_detect(*args, **kwargs):
    """
      True for valid representation of a mesh  
        FORMAT s = spm_mesh_detect(F)  
        F        - variable to query: filename, vol structure, patch structure  
        s        - true if F corresponds to a mesh, and false otherwise  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mesh_detect.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mesh_detect", *args, **kwargs)
