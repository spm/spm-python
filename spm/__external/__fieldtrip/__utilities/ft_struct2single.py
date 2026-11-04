from spm._runtime import Runtime


def ft_struct2single(*args, **kwargs):
    r"""
      FT_STRUCT2SINGLE converts all double precision numeric data in a structure  
        into single precision, which takes up half the amount of memory compared  
        to double precision. It will also convert plain matrices and cell-arrays.  
         
        Use as  
          x = ft_struct2single(x)  
         
        Starting from MATLAB 7.0, you can use single precision data in your  
        computations, i.e. you do not have to convert back to double precision.  
         
        MATLAB version 6.5 and older only support single precision for storing  
        data in memory or on disk, but do not allow computations on single  
        precision data. After reading a single precision structure from file, you  
        can convert it back with FT_STRUCT2DOUBLE.  
         
        See also FT_STRUCT2DOUBLE, FT_STRUCT2CHAR, FT_STRUCT2STRING  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/ft_struct2single.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_struct2single", *args, **kwargs)
