from spm._runtime import Runtime


def _fitsphere(*args, **kwargs):
    r"""
      FITSPHERE fits the centre and radius of a sphere to a set of points  
        using Taubin's method.  
         
        Use as  
              [center,radius] = fitsphere(pnt)  
        where  
          pnt     = Nx3 matrix with the Cartesian coordinates of the surface points  
        and  
          center  = the center of the fitted sphere  
          radius  = the radius of the fitted sphere  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/forward/private/fitsphere.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fitsphere", *args, **kwargs)
