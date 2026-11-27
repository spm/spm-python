from spm._runtime import Runtime


def _lapcal(*args, **kwargs):
    r"""
      LAPCAL computes the finite difference approximation to the surface laplacian  
        matrix using a triangulation of the surface  
         
        lap = lapcal(pnt, tri)  
         
        where  
          pnt   contains the positions of the vertices  
          tri   contains the triangle definition  
          lap   is the surface laplacian matrix  
         
        See also LAPINT, LAPINTMAT, READ_TRI, SAVE_TRI  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/lapcal.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("lapcal", *args, **kwargs)
