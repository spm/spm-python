from spm.__wrapper__ import Runtime


def pp_settings(*args, **kwargs):
    """
      Settings for push/pull  
        FORMAT sett = pp_settings(deg,bnd,ext)  
        deg - interpolation degree in each dimension (3 elements)  
              0 - nearest neighbour  
              1 - trilinear  
              2 - cubic B-spline  
              3 - 3rd degree B-spline  
              4 - 4th degree B-spline  
        bnd - boundary conditions in each dimension (3 elements)  
              0 - circulant  
              1 - reflected  
              2 - reflected negative  
        ext - extrapolation flag 0/1  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Spatial/pp_settings.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("pp_settings", *args, **kwargs)
