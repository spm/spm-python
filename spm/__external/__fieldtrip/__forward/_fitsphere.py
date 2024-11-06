from spm.__wrapper__ import Runtime


def _fitsphere(*args, **kwargs):
    """
      FITSPHERE fits the centre and radius of a sphere to a set of points  
        using Taubin's method.  
         
        Use as  
              [center,radius] = fitsphere(pnt)  
        where  
          pnt     = Nx3 matrix with the Carthesian coordinates of the surface points  
        and  
          center  = the center of the fitted sphere  
          radius  = the radius of the fitted sphere  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/fitsphere.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fitsphere", *args, **kwargs)
