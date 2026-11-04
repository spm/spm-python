from spm._runtime import Runtime


def _find_nearest(*args, **kwargs):
    r"""
      FIND_NEAREST finds the nearest vertex in a cloud of points and  
        does this efficiently for many target vertices at once (by means  
        of partitioning).  
         
        Use as  
          [nearest, distance] = find_nearest(pnt1, pnt2, npart)  
         
        See also KNNSEARCH, DIST, DSEARCHN  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/find_nearest.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("find_nearest", *args, **kwargs)
