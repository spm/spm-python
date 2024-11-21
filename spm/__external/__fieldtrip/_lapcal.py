from spm.__wrapper__ import Runtime


def _lapcal(*args, **kwargs):
    """
      LAPCAL computes the finite difference approximation to the surface laplacian  
        matrix using a triangulation of the surface  
         
        lap = lapcal(pnt, tri)  
         
        where  
          pnt   contains the positions of the vertices  
          tri   contains the triangle definition  
          lap   is the surface laplacian matrix  
         
        See also LAPINT, LAPINTMAT, READ_TRI, SAVE_TRI  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/lapcal.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("lapcal", *args, **kwargs)
