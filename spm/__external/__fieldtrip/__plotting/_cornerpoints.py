from spm.__wrapper__ import Runtime


def _cornerpoints(*args, **kwargs):
    """
      CORNERPOINTS returns the eight corner points of an anatomical volume  
        in voxel and in head coordinates  
         
        Use as  
          [voxel, head] = cornerpoints(dim, transform)  
        which will return two 8x3 matrices.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/private/cornerpoints.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cornerpoints", *args, **kwargs)
