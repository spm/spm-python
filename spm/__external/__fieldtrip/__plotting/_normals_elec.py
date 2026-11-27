from spm._runtime import Runtime


def _normals_elec(*args, **kwargs):
    r"""
      NORMALS_ELEC computes the surface normals for the electrodes from the given  
        triangulated headshape  
         
        Use as  
          nrm = normals_elec(elc, pos, tri)  
        where  
          elc = Kx3 matrix with the position of all electrodes  
          pos = Mx3 matrix with vertex locations of the triangulated headshape  
          tri = Nx3 matrix with the vertex indices for each of the triangles  
         
        See also PROJECT_ELEC, TRANSFER_ELEC, PCNORMALS  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/plotting/private/normals_elec.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("normals_elec", *args, **kwargs)
