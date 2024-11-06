from spm.__wrapper__ import Runtime


def spm_mesh_clusters(*args, **kwargs):
    """
      Label connected components of surface mesh data  
        FORMAT [C, N] = spm_mesh_clusters(M,T)  
        M        - a [mx3] faces array or a patch structure  
        T        - a [nx1] data vector (using NaNs or logicals), n = #vertices  
         
        C        - a [nx1] vector of cluster indices  
        N        - a [px1] size of connected components {in vertices}  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mesh_clusters.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mesh_clusters", *args, **kwargs)
