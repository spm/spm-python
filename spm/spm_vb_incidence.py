from spm._runtime import Runtime


def spm_vb_incidence(*args, **kwargs):
    r"""
      Edge-node incidence matrix of a graph  
        FORMAT A = spm_vb_incidence(edges,N)  
          
        edges    [Ne x 2] list of neighboring voxel indices  
        N        number of nodes (cardinality of node set)  
         
        Ne       number of edges (cardinality of edge set)  
        A        [Ne x N] matrix - is the discrete analogue of the grad operator  
        A(ij,k)  +1 if i=k, -1 if j=k, 0 otherwise, where ij is the edge   
        connecting nodes i and j, and k is in node set  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_vb_incidence.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_vb_incidence", *args, **kwargs)
