from spm.__wrapper__ import Runtime


def _megplanar_fitplane(*args, **kwargs):
    """
      Fit a plane through the B=f(x,y) plane and compute its two gradients  
        The first point in the plane is the gradiometer itself,  
        the neighbours are the subsequent points. This method also returns the  
        offset of the B-plane at each sensor, which is appriximately equal to the  
        field itself.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/megplanar_fitplane.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("megplanar_fitplane", *args, **kwargs)
