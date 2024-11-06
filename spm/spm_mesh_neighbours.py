from spm.__wrapper__ import Runtime


def spm_mesh_neighbours(*args, **kwargs):
    """
      Return first-order neighbours of all vertices of a surface mesh  
        FORMAT N = spm_mesh_neighbours(M,order)  
        M        - a patch structure or an adjacency matrix  
        order    - ordinal or euclidean distance for 1st order neighbours {[0],1}  
         
        N        - a [nxp] neighbours array (n = #vertices, p = # max neighbours)  
        D        - a [nxp] distance array to neighbours  
        N & D contain 0 when number of neighbours is smaller than p.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mesh_neighbours.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mesh_neighbours", *args, **kwargs)
