from spm._runtime import Runtime


def mne_mesh_edges(*args, **kwargs):
    r"""
      MESH_EDGES   Returns sparse matrix with edges number  
         
          SYNTAX  
              [EDGES] = MESH_EDGES(FACES)  
         
          faces : matrix of size [n_trianges, 3]  
          edges : sparse matrix of size [n_vertices, n_vertices]  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_mesh_edges.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_mesh_edges", *args, **kwargs)
