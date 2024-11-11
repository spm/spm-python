from spm.__wrapper__ import Runtime


def spm_mesh_inflate(*args, **kwargs):
    """
      Surface mesh inflation  
        FORMAT M = spm_mesh_inflate(M,T,S)  
         
        M        - surface mesh structure (see patch) or GIfTI object  
                   or handle to a patch in a figure  
        T        - number of time steps [default: Inf (auto)]  
        S        - update display every S time steps [default: 0 (never)]  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mesh_inflate.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mesh_inflate", *args, **kwargs)
