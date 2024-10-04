from spm.__wrap__ import _Runtime


def mne_mesh_edges(*args, **kwargs):
  """  MESH_EDGES   Returns sparse matrix with edges number  
     
      SYNTAX  
          [EDGES] = MESH_EDGES(FACES)  
     
      faces : matrix of size [n_trianges, 3]  
      edges : sparse matrix of size [n_vertices, n_vertices]  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_mesh_edges.m)
  """

  return _Runtime.call("mne_mesh_edges", *args, **kwargs)
