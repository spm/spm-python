from spm.__wrapper__ import Runtime


def _find_nearest(*args, **kwargs):
    """
      FIND_NEAREST finds the nearest vertex in a cloud of points and  
        does this efficiently for many target vertices at once (by means  
        of partitioning).  
         
        Use as  
          [nearest, distance] = find_nearest(pnt1, pnt2, npart)  
         
        See also KNNSEARCH, DIST, DSEARCHN  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/find_nearest.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("find_nearest", *args, **kwargs)
