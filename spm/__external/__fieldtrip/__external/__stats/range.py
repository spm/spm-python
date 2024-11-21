from spm.__wrapper__ import Runtime


def range_(*args, **kwargs):
    """
      RANGE computes the range (i.e. difference between min and max) for a vector  
        or an N-dimensional array.   
         
        Use as  
          r = range(x)  
        or you can also specify the dimension along which to look by  
          r = range(x, dim)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/external/stats/range.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("range", *args, **kwargs)
