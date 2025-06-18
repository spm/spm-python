from mpython import Runtime


def spm_mesh_edges(*args, **kwargs):
    """
      Return edges of a surface mesh
        FORMAT [E,L] = spm_mesh_edges(M)
        M        - a [nx3] faces array or a patch handle/structure

        E        - a [mx2] edges array
        L        - a [m,1] edge length vector
                   Only available if M is a patch structure.
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mesh_edges.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mesh_edges", *args, **kwargs)
