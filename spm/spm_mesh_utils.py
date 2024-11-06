from spm.__wrapper__ import Runtime


def spm_mesh_utils(*args, **kwargs):
    """
      A gateway function for surface mesh-related compiled algorithms   
         
        FORMAT [N, D] = spm_mesh_utils('neighbours',A)  
        Return an array of first-order neighbours given an adjacency matrix  
         
        FORMAT Fi = spm_mesh_utils('neighbouringfaces',F,i)  
        Return the indices of the neighbouring triangles of a given triangle  
          
        FORMAT D = spm_mesh_utils('dijkstra',N,D,i,dmax)  
        Compute geodesic distance on a triangular mesh using Dijkstra algorithm  
         
        FORMAT V = spm_mesh_utils('volume',M)  
        Compute the volume of a closed surface mesh  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mesh_utils.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mesh_utils", *args, **kwargs)
