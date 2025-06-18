from mpython import Runtime


def mne_mesh_edges(*args, **kwargs):
    """
      MESH_EDGES   Returns sparse matrix with edges number

          SYNTAX
              [EDGES] = MESH_EDGES(FACES)

          faces : matrix of size [n_trianges, 3]
          edges : sparse matrix of size [n_vertices, n_vertices]


    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_mesh_edges.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_mesh_edges", *args, **kwargs)
