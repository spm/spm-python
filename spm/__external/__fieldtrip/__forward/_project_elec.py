from spm._runtime import Runtime


def _project_elec(*args, **kwargs):
    r"""
      PROJECT_ELEC projects electrodes on a triangulated surface  
        and returns triangle index, la/mu parameters and distance  
         
        Use as  
          [el, prj] = project_elec(elc, pnt, tri)  
        with  
          elc = Kx3 matrix with the position of all electrodes  
          pos = Mx3 matrix with the vertex locations of the triangulated headshape  
          tri = Nx3 matrix with the vertex indices for each of the triangles  
         
        This function returns   
          el    = Nx4 matrix with [tri, la, mu, dist] for each electrode  
          prj   = Nx3 matrix with the projected electrode position  
         
        See also TRANSFER_ELEC  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/forward/private/project_elec.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("project_elec", *args, **kwargs)
