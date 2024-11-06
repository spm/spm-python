from spm.__wrapper__ import Runtime


def spm_mesh_max(*args, **kwargs):
    """
      Sizes, local maxima and locations of excursion sets on a surface mesh  
        FORMAT [N,Z,M,A,XYZ] = spm_mesh_max(X,L,G)  
        X        - a [nx1] array of stat values  
        L        - a [nx1] array of locations {in vertices}  
        G        - a patch structure  
         
        N        - a [px1] size of connected components {in vertices}  
        Z        - stat values of maxima  
        M        - location of maxima {in vertices}  
        A        - region number  
        XYZ      - cell array of vertices locations  
       __________________________________________________________________________  
         
        See also: spm_max.m, spm_mesh_clusters.m and spm_mesh_get_lm.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mesh_max.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mesh_max", *args, **kwargs)
