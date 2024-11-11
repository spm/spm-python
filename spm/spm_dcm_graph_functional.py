from spm.__wrapper__ import Runtime


def spm_dcm_graph_functional(*args, **kwargs):
    """
      Functional graph display  
        FORMAT spm_dcm_graph_functional(A,V)  
        FORMAT spm_dcm_graph_functional(V) - metric MDS  
        A     - (m x m) weighted adjacency matrix  
        V     - (n x m) locations in (nD) Multidimensional Scaling (MDS) Space   
         
        If V is not specified the Weighted Graph Laplacian of A is used with  
        metric MDS to define the functional space.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_graph_functional.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_graph_functional", *args, **kwargs, nargout=0)
