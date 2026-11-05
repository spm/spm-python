from spm._runtime import Runtime


def _transfer_elec(*args, **kwargs):
    r"""
      TRANSFER_ELEC computes the transfer matrix from vertex to electrode potentials  
        using bi-linear interpolation over the triangles.  
         
        Use as  
          tra = transfer_elec(el, pos, tri)  
        where  
          el  = Kx3 matrix that contains the [tri, la, mu] for each electrode  
          pos = Mx3 matrix with vertex locations of the triangulated headshape  
          tri = Nx3 matrix with the vertex indices for each of the triangles  
         
        See also PROJECT_ELEC, NORMALS_ELEC  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/forward/private/transfer_elec.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("transfer_elec", *args, **kwargs)
