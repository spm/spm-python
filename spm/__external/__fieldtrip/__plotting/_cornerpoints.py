from spm._runtime import Runtime


def _cornerpoints(*args, **kwargs):
    r"""
      CORNERPOINTS returns the eight corner points of an anatomical volume  
        in voxel and in head coordinates  
         
        Use as  
          [voxel, head] = cornerpoints(dim, transform)  
        which will return two 8x3 matrices.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/plotting/private/cornerpoints.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("cornerpoints", *args, **kwargs)
