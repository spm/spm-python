from spm._runtime import Runtime


def _megplanar_fitplane(*args, **kwargs):
    r"""
      Fit a plane through the B=f(x,y) plane and compute its two gradients  
        The first point in the plane is the gradiometer itself,  
        the neighbours are the subsequent points. This method also returns the  
        offset of the B-plane at each sensor, which is appriximately equal to the  
        field itself.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/megplanar_fitplane.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("megplanar_fitplane", *args, **kwargs)
