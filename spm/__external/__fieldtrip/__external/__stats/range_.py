from spm._runtime import Runtime


def range_(*args, **kwargs):
    r"""
      RANGE computes the range (i.e. difference between min and max) for a vector  
        or an N-dimensional array.   
         
        Use as  
          r = range(x)  
        or you can also specify the dimension along which to look by  
          r = range(x, dim)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/external/stats/range.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("range", *args, **kwargs)
