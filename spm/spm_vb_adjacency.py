from spm.__wrapper__ import Runtime


def spm_vb_adjacency(*args, **kwargs):
    """
      (Weighted) adjacency (or weight) matrix of a graph  
        FORMAT W = spm_vb_adjacency(edges,weights,N)  
         
        edges    [Nedges x 2] list of neighboring voxel indices  
        weights  [Nedges x 1] list of edge weights (unity of not specified)  
        N        number of nodes (cardinality of node set)  
         
        W        [N x N] matrix of (weighted) edges  
        Wij      edge weight between nodes i and j if they are neighbors, otherwise 0  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_vb_adjacency.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_vb_adjacency", *args, **kwargs)
